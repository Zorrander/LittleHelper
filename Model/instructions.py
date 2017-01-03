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
            action:     FORWARD, BACKWARD, STOP
            direction:  LEFT, RIGHT
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

    @property
    def action(self):
        return self.action

    @property
    def direction(self):
        return self.direction

    @property
    def speed(self):
        return self.speed

    @property
    def angle(self):
        return self.angle

    @property
    def distance(self):
        return self.distance

    @property
    def sleep_time(self):
        return self.sleep_time
