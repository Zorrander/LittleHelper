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

    def update_current_instruction(self):
        """
        """
        flag = False
        current_distance = (self.distance[0] + self.distance[1])/2
        print(str(self.distance[0]) + " - " + str(self.distance[1]) + "current distance : " +str(current_distance))
        # si on parcouru la distance recherché 
        if(self.instructions_list[0].get_distance() <= current_distance):
            self.del_first_instruction() # on passe a l'action suivante
            flag = True
            
        return flag
            

        

        
        

