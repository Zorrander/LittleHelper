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

    def fillFrame():
        """

            The fillFrame function
            ----------------------

            used to send information about the battery to the STM32

        """
        tmp = ''

        while ( len(str(tmp)) < 8 ):
            tmp = '0' + tmp

        return tmp

    def __init__(self):
       self.charged = True


