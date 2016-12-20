#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The motor module
    ================

    Used to handle the behaviours of motors on the car.

"""

class FrontMotor():

    """

        The Front motor class
        ---------------------

        Adapt the generic behaviour of Motor to control the direction of the car

    """

    def __init__(self):
        self.angle = 0

    def turnLeft(self, angle):
        self.angle = angle

    def turnRight(self, angle):
        self.angle = -angle

    @property
    def angle(self):
        return self.angle

class RearMotor():

    """

        The Front motor class
        ---------------------

        Adapt the generic behaviour of Motor to move the car

    """

    def __init__(self):
        self.speed = 0

    def moveForward(self, speed):
        self.speed = speed

    def moveBackward(self, speed):
        self.speed = -speed

    def stop(self):
        self.speed = 0

    @property
    def speed(self):
        return self.speed
