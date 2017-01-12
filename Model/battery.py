#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The battery module
    ===================

    Used to represent the battery of our car

"""

class Battery():
    """
    """
    
    def __init__(self):
       self.charged = True

    @property
    def charged(self):
        """
            The state of the battery

            :getter: Returns the state of the battery
            :setter: Sets the state of the battery
            :type: Boolean
        """
        return self.charged
