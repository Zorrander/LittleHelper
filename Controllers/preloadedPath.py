#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The PreloadedPaths module
    =========================

    Used to represent the list of paths

"""

import time
from Model.path import Path, Paths
from threading import Thread
from constant import FORWARD, BACKWARD, STOP, LEFT, RIGHT

class PreloadedPaths(Thread):

    """
        The PreloadedPaths class
        --------------
    """

    def __init__(self, model):
        Thread.__init__(self)
        self.model = model
        self.paths = Paths()
        self.current_path = Path()
        self.run_path = False

    def start_path(self, index):
        self.current_path = self.paths.get_path(index)
        self.run_path = True

    def run(self):
        """
        Control the progress of the path
        """
        while(1):
            if(self.run_path):
                if (len(self.current_path.get_path()) != 0):
                    inst = self.current_path.current_instruction

                    # action stop
                    if(inst.action == STOP):
                        self.stop_car(inst.sleep_time)
                    # action move
                    else:
                        self.move_car(inst.action, inst.speed, inst.direction, inst.angle, inst.distance)
                else:
                    # We stop the car if the path is ended
                    self.model.car.moveForward(0)
                    self.run = False


    def stop_car(self, sleep_time):
        # we stop the car
        self.model.car.moveForward(0)
        # Sleep
        time.sleep(time_sleep)
        # We go on to the next action
        self.path_copy.del_first_instruction()


    def move_car(self, action, speed, direction, angle, distance):

        if(action == FORWARD):
            self.model.car.moveForward(speed)
        else:
            self.model.car.moveBackward(speed)

        if(direction == LEFT):
            self.model.car.turnLeft(angle)
        else:
            self.model.car.turnRight(angle)

        # See if the distance is reach
        distance_traveled = self.model.distance
        self.distance_management(distance, distance_traveled)

    def distance_management(self, distance, distance_traveled):
        if(distance <= distance_traveled):
            self.model.reset_distance = True
            while(self.model.reset_distance):
                pass
            self.path_copy.del_first_instruction()

    def stop_path(self):
        self.run_path = False
