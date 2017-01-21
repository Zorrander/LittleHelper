#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The PreloadedPaths module
    =========================

    Used to manage the processing of the paths

"""

import time
from Model.path import Path, Paths
from threading import Thread
from constant import FORWARD, BACKWARD, STOP, SLEEP_PRELOADEDPATH_THREAD, NON_BLOCKING

class PreloadedPaths(Thread):
    """
        The PreloadedPaths is composed of :
            >>> 1 model world
            >>> 1 list of paths
            >>> 1 current path
    """

    def __init__(self, model):
        Thread.__init__(self)
        self.model = model
        self.paths = Paths()
        self.current_path = Path()
        self.run_path = False
        self.terminated = False

    def start_path(self, index):
        """
            Allow to choose the index of the path we want to follow

            :param index: the index of the path
            :type index: int
        """
        self.current_path = self.paths.get_path(index)
        # Set the reset distance flag and reset the ack
        self.model.reset_distance = True
        self.model.ack_reset_distance = False

        # While we didn't receive the ack we wait
        while(not(self.model.ack_reset_distance)):
            pass

        time.sleep(0.01)
        self.run_path = True


    def run(self):
        """
            Run function of the thread.
            The function that is launch when we start the thread.
            Control the progress of the path.
        """
        while not self.terminated:
            # If a path is running
            if(self.run_path):

                # If the path still have instructions
                if (len(self.current_path.get_path()) != 0):
                    inst = self.current_path.get_current_instruction()
                    # action stop
                    if(inst.action == STOP):
                        self.stop_car(inst.sleep_time)
                    # action move
                    else:
                        self.move_car(inst.action, inst.speed, inst.distance)

                # If a path is empty (ie all the instruction are done) we stop the car
                else:
                    self.model.car.moveForward(0)
                    self.run_path = False

            # Sleep periode to let the hand to an other thread
            time.sleep(SLEEP_PRELOADEDPATH_THREAD)


    def stop_car(self, sleep_time):
        """
            Stop the car during the time indicated.

            :param sleep_time: time to stop in seconds
            :type sleep_time: float
        """
        # we stop the car
        self.model.car.moveForward(0)
        # Sleep
        time.sleep(sleep_time)
        # We go on to the next action
        self.current_path.del_first_instruction()


    def move_car(self, action, speed, distance):
        """
            Move the car according to the action (forward, backward, turn left, turn right)

            :param action: action to execute
            :type action: FORWARD, BACKWARD, TURN_LEFT, TURN_RIGHT
            :param speed: speed for moving backward or forward
            :type speed: int
            :param distance: the distance to traveled
            :type distance: int
        """
        if(action == FORWARD):
            self.model.car.moveForward(speed)
            # Turn according to the angle detect by the camera
            #self.model.car.turn(self.model.car.direction_motor.angle_camera)

            # See if the distance is reach
            distance_traveled = self.model.current_distance
            self.distance_management(distance, distance_traveled)
        elif(action == BACKWARD):
            self.model.car.moveBackward(speed)
            # Turn according to the angle detect by the camera
            self.model.car.turn(self.model.car.direction_motor.angle_camera)

            # See if the distance is reach
            distance_traveled = self.model.current_distance
            self.distance_management(distance, distance_traveled)
        elif(action == 3):#TURN_LEFT):
            self.bend(1)
        elif(action == 4):#TURN_RIGHT):
            self.bend(-1)

    def distance_management(self, distance, distance_traveled):
        """
            Manage the distance.
            If a band is detected we update the distance_traveled to be more precise.
            If the distance ordered by the instruction is reach we can go to the next instruction.

            :param distance: distance to reach
            :type distance: int
            :param distance_traveled: distance traveled by the car
            :type distance_traveled: float
        """
        # If we saw a band
        if(self.model.sema_distance.acquire(NON_BLOCKING)):
            print("preloaded path : sema distance")
            # Set the reset distance flag and reset the ack
            self.model.reset_distance = True
            self.model.ack_reset_distance = False
        
            # While we didn't receive the ack we wait
            while(not(self.model.ack_reset_distance)):
                pass
            print("preloaded path : remis à zéro")
            # update the new distance to traveled
            # self.current_path.get_current_instruction().distance = distance - self.model.real_distance
        
            print("preloaded path : test sema_distance")
        # If the distance of the instruction is reach
        if(distance <= distance_traveled):
            # Set the reset distance flag and reset the ack
            self.model.reset_distance = True
            self.model.ack_reset_distance = False

            # While we didn't receive the ack we wait
            while(not(self.model.ack_reset_distance)):
                pass

            # FIXME: I don't know why but if we don't put the sleep
            # the next action begin before the distance is reset
            time.sleep(0.01)

            self.current_path.del_first_instruction()


    def stop_path(self):
        """
            Allow to stop the path at any moment.
            In this case the car stop.
        """
        self.run_path = False
        self.model.car.moveForward(0)


    def bend(self, direction):
        """
            ALlow to turn an 90° angle on the right or on the left.
            The turn has to begin 120cm before the bend.

            :param direction: the direction to turn (-1 : right, 1 : left)
            :type direction: int
        """
        # Turn to the right
        if(direction == -1):
            self.model.car.turnRight(45)
            self.model.car.moveForward(40)
        # Turn to the left
        elif(direction == 1):
            self.model.car.turnLeft(45)
            self.model.car.moveForward(40)

        time.sleep(13)

        self.model.car.turn(0)

        time.sleep(2)

        self.current_path.del_first_instruction()

    def stop(self):
        """
            Allow to stop the thread and quit it.
            In this case we stop the car
        """
        self.model.car.moveForward(0)
        self.terminated = True
