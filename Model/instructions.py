#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The Instruction module
    ======================

    Used to represent the instructions the car is going to execute when going from point A to B

"""

class Instruction():

    """
    The Instruction class
    ---------------------

    Caracteristics :
       >>> an action to execute
       >>> specification
    """

    def __init__(self, action, direction, speed, angle, distance, sleep_time):
        """
            action:     0 forward
                        1 backward
                        2 stop

            direction:  0 left
                        1 right

            speed:      speed of the rear motors

            angle:      angle of the front motor

            distance:   distance to travel

            sleep_time: time to wait if the action is sleep

        """
        self.action = action
        self.direction = direction
        self.speed = speed
        self.angle = angle
        self.distance = distance
        self.sleep_time = sleep_time

    def get_action(self):
        return self.action

    def get_direction(self):
        return self.direction

    def get_speed(self):
        return self.speed

    def get_angle(self):
        return self.angle

    def get_distance(self):
        return self.distance

    def get_sleep_time(self):
        return self.sleep_time
