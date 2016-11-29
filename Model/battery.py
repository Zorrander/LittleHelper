#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The battery module
    ===================

    Used to represent the battery of our car

"""

import sys


class Battery():

    """

        The battery class
        -----------------

        Caracteristics :
            >>> 1 attribut
            >>> 1 function

    """

    def __init__(self):
       self.charged = True

    def set_charged(value):
        if(value == 1):
            self.charged = True
        else:
            self.charged = False     


