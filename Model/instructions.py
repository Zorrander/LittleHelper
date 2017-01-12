#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The Instruction module
    ======================

    Used to represent the instructions the car is going to execute when going from point A to B

"""

class Instruction():
    """
    Caracteristics :
       >>> an action to execute
       >>> specification
    """

    def __init__(self, action, speed=0, distance=0, sleep_time=0):
        """
            :param action: the action to execute FORWARD, BACKWARD, STOP, TURN_LEFT, TURN_RIGHT
            :type action: FORWARD, BACKWARD, STOP, TURN_LEFT, TURN_RIGHT
            :param speed: the speed of the rear motors
            :type speed: int
            :param distance: distance to travel
            :type distance: int
            :param sleep_time: time to wait if the action is sleep
            :type sleep_time: int

        """
        self.action = action
        self.speed = speed
        self.distance = distance
        self.sleep_time = sleep_time

    @property
    def action(self):
        """
            The action of the instruction

            :getter: Returns the action of the instruction
            :setter: Sets the action of the instruction
            :type: FORWARD, BACKWARD, STOP, TURN_LEFT, TURN_RIGHT
        """
        return self.action

    @property
    def speed(self):
        """
            The speed of the instruction

            :getter: Returns the speed of the instruction
            :setter: Sets the speed of the instruction
            :type: int
        """
        return self.speed

    @property
    def distance(self):
        """
            The distance of the instruction

            :getter: Returns the distance of the instruction
            :setter: Sets the distance of the instruction
            :type: int
        """
        return self.distance

    @property
    def sleep_time(self):
        """
            The time to sleep (to stop the car)

            :getter: Returns the time to sleep
            :setter: Sets the time to sleep
            :type: int
        """
        return self.sleep_time
