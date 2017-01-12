#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The world module
    ===================

    Used to represent the world

"""

import threading
from car import Car
from path import Path

class World():

    def __init__(self, car):
        """
            The world is composed of :
                >>> 1 car
                >>> 1 path
                >>> 1 current distance traveled
                >>> 1 boolean to reset the disatance
                    1 boolean to confirm the reset
        """

        self.car = car
        self.path = Path()

        # Distance management
        self.current_distance = 0
        self.real_distance = 0
        self.reset_distance = False
        self.ack_reset_distance = False

        # ==========================
        # Semaphore used in the code
        # ==========================

        # semaphore[1] shared with spi process
        self.sema_distance = threading.Semaphore()
        # semaphore[1] shared with video process
        self.sema_band_xcoord = threading.Semaphore()


    @property
    def car(self):
        return self.car

    @property
    def path(self):
        return self.path

    @property
    def current_distance(self):
        return self.current_distance

    @property
    def real_distance(self):
        return self.real_distance

    @property
    def reset_distance(self):
        return self.reset_distance

    @property
    def ack_reset_distance(self):
        return self.ack_reset_distance

    def set_distance(self, distance1, distance2):
        self.current_distance = (distance1 + distance2)/2
