#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The Instruction module
    ======================

    Used to represent the instructions the car is going to execute when going from point A to B
    
"""

class Instruction():

    """
    The Instruction class
    ---------------------

    Caracteristics :
       >>> an action to execute 
       >>> specification 	
    """
    
    def __init__(self, action, speed, angle, distance):
	self.action = action
	self.speed = speed
        self.angle = angle
        self.distance = distance

    def get_distance(self):
        return self.distance

    def get_angle(self):
        return self.angle

    def get_speed(self):
        return self.speed

    def get_action(self):
        return self.action
