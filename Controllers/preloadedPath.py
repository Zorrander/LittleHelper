#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The PreloadedPaths module
    =========================

    Used to represent the list of paths

"""
from Model import path
from Model import instructions
import time

class PreloadedPaths():

    """
        The path class
        --------------
        Caracteristics :
            >>> X attribut
            >>> X function
    """

    def __init__(self, model):
        self.model = model
        self.list_paths = []
        print("__init__ preloaded path")
        self.build_list()
        self.path_copy = path.Path()


    def build_list(self):
        """
        Build the list of the preloadedPath
        """
        # Instruction(action, direction, speed, angle, distance, sleep_time)
        # action
        forward = 0
        backward = 1
        stop = 2
        # direction
        left = 0
        right = 1

        # ====================================================================
        #                      Creation of the first path
        # ====================================================================
        # creation of the instructions
            # forward 100 cm - left 0°
        inst1 = instructions.Instruction(forward, left, 35, 0, 100, 0)
            # forward 150 cm - left 40°
        inst2 = instructions.Instruction(forward, left, 35, 40, 150, 0)
            # forward 200 cm - left 0°
        inst3 = instructions.Instruction(forward, left, 35, 0, 200, 0)
            # stop
        inst4 = instructions.Instruction(stop, left, 0, 0, 0, 5)

        # creation of the path
        new_path = path.Path()
        new_path.add_instruction(inst1)
        new_path.add_instruction(inst2)
        new_path.add_instruction(inst3)
        new_path.add_instruction(inst4)

        self.list_paths.append(new_path)

    def start_path(self, index):

        self.path_copy = self.list_paths[index]
        self.model.set_path(self.path_copy)
        self.start_moving()

    def start_moving(self):
        """
        Control the progress of the path

        Case action = Stop
            We stop the car, the angle of the wheels don't change
        """
#        while(1):
           # if (len(self.path_copy.get_path()) != 0):
            while (len(self.path_copy.get_path()) != 0):
                # flag that check if an action end during the loop
                flag = False

                # Current instruction and action
                current_instruction = self.path_copy.get_current_instruction()
                current_action = current_instruction.get_action()

                # action is stop
                if(current_action == 2):
                    # we stop the car
                    self.model.moveForward(0)

                    # Sleep
                    time_sleep = current_instruction.get_sleep_time()
                    time.sleep(time_sleep)

                    # We go on to the next action
                    self.path_copy.del_first_instruction()
                    flag = True

                else:
                    # get the parameters
                    speed = current_instruction.get_speed()
                    direction = current_instruction.get_direction()
                    angle = current_instruction.get_angle()

                    # action is forward
                    if(current_action == 0):
                        self.model.moveForward(instruction_speed) # Move the car
                    # action is backward
                    else:
                        self.model.moveBackward(instruction_speed) # Move the car

                    # direction is left
                    if(direction == 0):
                        self.model.turnLeft(angle)
                    # direction is right
                    else:
                        self.model.turnRight(angle)

                    # manage the distance
                    distance_to_travel = current_instruction.get_distance()
                    distance_traveled = self.model.get_distance()
                    if(distance_to_travel <= distance_traveled):
                        self.path_copy.del_first_instruction()
                        flag = True

                # if an action end during the loop
                if(flag):
                    # we ask the distance to be reset
                    self.model.reset_distance()
                    # and wait for the ack of the STM
                    while(self.model.get_distance_ack()):
                        pass
