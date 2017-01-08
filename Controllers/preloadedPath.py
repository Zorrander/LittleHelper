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
from constant import FORWARD, BACKWARD, STOP, LEFT, RIGHT, \
    SLEEP_PRELOADEDPATH_THREAD, NON_BLOCKING

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
                    inst = self.current_path.get_current_instruction()

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

                # Sleep periode to let the hand to an other thread
                time.sleep(SLEEP_PRELOADEDPATH_THREAD)


    def stop_car(self, sleep_time):
        # we stop the car
        self.model.car.moveForward(0)
        # Sleep
        time.sleep(sleep_time)
        # We go on to the next action
        self.current_path.del_first_instruction()


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
        distance_traveled = self.model.current_distance
        self.distance_management(distance, distance_traveled)

    def distance_management(self, distance, distance_traveled):
        # If we saw a band
        if(self.model.sema_distance.acquire(NON_BLOCKING)):
            # Set the reset distance flag and reset the ack
            self.model.reset_distance = True
            self.model.ack_reset_distance = False

            # While we didn't receive the ack we wait
            while(not(self.model.ack_reset_distance)):
                pass

            # update the new distance to traveled
            self.current_path.get_current_instruction().distance = distance - self.model.real_distance

            # We release the semaphore
            self.model.sema_distance.release()

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
        self.run_path = False
