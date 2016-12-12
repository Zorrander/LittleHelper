#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The motor module
    ================

    Used to handle the behaviours of motors on the car.

"""

import sys
from abc import ABCMeta, abstractmethod

LEFT=0
RIGHT=128
FORWARD = 0
BACKWARD = 128


class FrontMotor():

    """

        The Front motor class
        ---------------------

        Adapt the generic behaviour of Motor to control the direction of the car

    """

    def __init__(self):
        self.state = 0
        self.angle = 0 

    def notify(self):
        pass

    def turnLeft(self, angle):
        print("turnLeft")
        self.state = LEFT
        self.angle = angle

    def turnRight(self, angle):
        print("turnRight")
        self.state = RIGHT
        self.angle = angle

    def getState(self):
        return self.state

    def getAngle(self):
        return self.angle

class RearMotor():

    """

        The Front motor class
        ---------------------

        Adapt the generic behaviour of Motor to move the car

    """

    def __init__(self):
        self.state = 0 
        self.speed = 0

    def moveForward(self, speed):
        self.state = FORWARD
        self.speed = speed

    def moveBackward(self, speed):
        print("moveBackward")
        self.state = BACKWARD
        self.speed = speed

    
    def stop(self):
        print("stop")
        self.speed = 0
    
    def notify(self):
        pass

    def getState(self):
        return self.state

    def getSpeed(self):
        return self.speed


