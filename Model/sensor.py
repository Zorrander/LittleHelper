#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The sensor module
    =================

    Used to handle the behaviour of sensors on the car.

"""

import sys
from abc import ABCMeta, abstractmethod


class Sensor:

    """

        The Sensor abstract class
        -------------------------

        Caracteristics :
            >>>
            >>>
    """
    __metaclass__ = ABCMeta


    @abstractmethod
    def notify():
          pass

    def fillFrame():

        tmp = ''

        while ( len(str(tmp)) < 8 ):
            tmp = '0' + tmp

        return tmp



class MagneticSensor(Sensor):

    """

        The MagneticSensor class
        ------------------------

        Adapt the generic behaviour of Sensor to the magnetic sensors of the car.

    """

    def __init__(self):
        super(self.__class__, self).__init__()

    def notify():
        pass


class UltrasoundSensor(Sensor):

    """

        The ultrasound sensor class
        ---------------------------

        Adapt the generic behaviour of Sensor to the ultrasound sensors of the car.

    """

    def __init__(self):
        super(self.__class__, self).__init__()
        self.distance = 0

    def notify():
        pass
    
    def set_distance(distance):
        self.distance = distance
