#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The observable module
    ===================

    Used to apply the Observer patter in the application
"""

import sys

class Observable:

    def __init__(self):
        self.__observers = []


    def register_observer(self, observer):
        self.__observers.append(observer)


    def notify_distance_observers(self, distance):
        for observer in self.__observers:
            observer.notify_distance(self, distance)
