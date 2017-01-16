#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The sensor module
    =================

    Used to handle the behaviour of sensors on the car.

"""

class UltrasoundSensor():
    """
        Used to represente the ultrasound sensors of the car.

        Caracteristics :
            >>> a distance
            >>> a name
    """

    def __init__(self, name):
        self.distance = 0
        self.name = name

    @property
    def name(self):
        """
            The name of the sensor

            :getter: Returns the name of the sensor
            :setter: Sets the name of the sensor
            :type: str
        """
        return self.name

    @property
    def distance(self):
        """
            The distance catch by the sensor

            :getter: Returns the distance
            :setter: Sets the distance
            :type: int
        """
        self.distance = distance
