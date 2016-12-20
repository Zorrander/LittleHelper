#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The sensor module
    =================

    Used to handle the behaviour of sensors on the car.

"""

class UltrasoundSensor(Sensor):

    """

        The ultrasound sensor class
        ---------------------------

        Adapt the generic behaviour of Sensor to the ultrasound sensors of the car.

    """

    def __init__(self, name):
        self.distance = 0
        self.name = name

    @property
    def name(self):
        return self.name

    @property
    def distance(self):
        self.distance = distance
        
