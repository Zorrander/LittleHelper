#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The motor module
    ================

    Used to handle the behaviours of motors on the car.

"""

import sys
from abc import ABCMeta, abstractmethod


class FrontMotor():

    """

        The Front motor class
        ---------------------

        Adapt the generic behaviour of Motor to control the direction of the car

    """

    def __init__(self):
        self.angle = 0 

    def notify(self):
        pass

    def turnLeft(self, angle):
        print("turnLeft")
        self.angle = angle

    def turnRight(self, angle):
        print("turnRight")
        self.angle = -angle

    def getAngle(self):
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
        print("moveForward")
        self.speed = speed

    def moveBackward(self, speed):
        print("moveBackward")
        self.speed = -speed

    
    def stop(self):
        print("stop")
        self.speed = 0
    
    def notify(self):
        pass

    def getSpeed(self):
        return self.speed


