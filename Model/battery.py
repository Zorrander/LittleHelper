#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The battery module
    ===================

    Used to represent the battery of our car

"""

class Battery():

    """

        The battery class
        -----------------

    """

    def __init__(self):
       self.charged = True

    @property
    def cherged(self):
        return self.charged
