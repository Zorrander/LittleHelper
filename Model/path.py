#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The path module
    ===============
    Used to represent the path
    
"""

class Path():

    """
        The path class
        --------------
        Caracteristics :
            >>> X attribut
            >>> X function
    """
    
    def __init__(self):
        """
        """
        # list of instructions corresponding to the path
        self.instructions_list = []
        self.distance = [0,0]
        self.flag = False

    def add_instruction(self, instruction):
        """
        """
        self.instructions_list.append(instruction)

    def del_first_instruction(self):
        """
        """
        del self.instructions_list[0]

    def get_path(self):
        """
        """
        return self.instructions_list

    def get_current_instruction(self):
        """
        """
        return self.instructions_list[0]

    def set_distance(self, left_distance, right_distance):
        self.distance[0] = left_distance
        self.distance[1] = right_distance
        
    def get_current_distance(self):
        current_distance = (self.distance[0] + self.distance[1])/2  
        return current_distance

        

        
        

