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

    def update_current_instruction(self):
        """
        """
        current_distance = (self.distance[0] + self.distance[1])/2
        # si on parcouru la distance recherché 
        if(self.instructions_list[0].get_distance() == current_distance):
            del_first_instruction(self) # on passe a l'action suivante
            if (self.instructions_list):
                pass 
                #updateModel() 
        # si on parcouru plus que la distance recherché
        elif(current_distance > self.instructions_list[0].get_distance()):
            del_first_instruction(self)
            print ("Too far, careful")

        

        
        

