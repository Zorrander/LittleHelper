#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The PreloadedPaths module
    =========================

    Used to represent the list of paths

"""
from Model import path
from Model import instructions
from threading import Thread
import time


# Instruction(action, direction, speed, angle, distance, sleep_time)
# action
FORWARD = 0
BACKWARD = 1
STOP = 2
# direction
LEFT = 0
RIGHT = 1

class PreloadedPaths(Thread):

    """
        The path class
        --------------
        Caracteristics :
            >>> X attribut
            >>> X function
    """

    def __init__(self, model):
        Thread.__init__(self)
        self.model = model
        self.list_paths = []
        self.build_list()
        self.path_copy = path.Path()


    def build_list(self):
        """
        Build the list of the preloadedPath
        """

        # ====================================================================
        #                      Creation of the first path
        # ====================================================================
        # creation of the instructions
            # forward 100 cm - left 0°
        inst1 = instructions.Instruction(FORWARD, LEFT, 35, 0, 200, 0)
            # forward 50 cm - left 40°
        inst2 = instructions.Instruction(FORWARD, LEFT, 35, 40, 150, 0)
            # forward 200 cm - left 0°
        inst3 = instructions.Instruction(FORWARD, LEFT, 35, 0, 100, 0)
            # stop
        inst4 = instructions.Instruction(STOP, LEFT, 0, 0, 0, 5)

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

    def run(self):
        """
        Control the progress of the path

        Case action = Stop
            We stop the car, the angle of the wheels don't change
        """
        while(1):
            if (len(self.path_copy.get_path()) != 0):
#            while (len(self.path_copy.get_path()) != 0):
                # flag that check if an action end during the loop
 #               flag = False

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
#                    flag = True

                else:
                    # get the parameters
                    speed = current_instruction.get_speed()
                    direction = current_instruction.get_direction()
                    angle = current_instruction.get_angle()
                    # get the distances
                    distance_to_travel = current_instruction.get_distance()
                    distance_traveled = self.model.get_distance()

                    # action is forward
                    if(current_action == FORWARD):
                        self.model.moveForward(speed)
                    # action is backward
                    else:
                        self.model.moveBackward(speed)

                    # direction is left
                    if(direction == LEFT):
                        self.model.turnLeft(angle)
                    # direction is right
                    else:
                        self.model.turnRight(angle)

                    # manage the distance
                    if(distance_to_travel <= distance_traveled):
                        print("distance to travel : "+str(distance_to_travel)+" - distance traveled : "+str(distance_traveled))
                        
                        self.model.reset_distance()
                        while(self.model.get_distance_ack() == 0):
                            test = 0
                        
                        self.path_copy.del_first_instruction()
