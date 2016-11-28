#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The observer module
    ===================

    Used to apply the Observer patter in the application
"""

import sys

class Observer:

    def __init__(self, observable):
        observable.register_observer(self)

    def notify(self, observable, *args, **kwargs):
        print('Got', args, kwargs, 'From', observable)
