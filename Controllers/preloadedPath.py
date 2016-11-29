
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The PreloadedPaths module
    =========================

    Used to represent the list of paths
    
"""
from Model import path
from Model import instructions

class PreloadedPaths():

    """
        The path class
        --------------
        Caracteristics :
            >>> X attribut
            >>> X function
    """
    
    def __init__(self, model):
        self.model = model
        self.list_paths = []
        print("__init__ preloaded path")
        self.build_list()
 

    def build_list(self):
        forward_left = 0
        forward_right = 1 
        backward_left = 2
        backward_right = 3
        forward = 4
        backward = 5
        instruct_move = instructions.Instruction(forward, 35, 0, 300) 
        instruct_move_fast = instructions.Instruction(forward, 75, 0, 300)
        instruct_stop = instructions.Instruction(forward, 0, 0, 0)
        instruct_turn_left = instructions.Instruction(forward_left, 10, 40, 50)
        instruct_turn_right = instructions.Instruction(forward_right, 10, 40, 50)

        new_path = path.Path()
        new_path.add_instruction(instruct_move)
        new_path.add_instruction(instruct_stop)
        new_path.add_instruction(instruct_turn_left)
        new_path.add_instruction(instruct_stop)
      
        self.list_paths.append(new_path)
        print("Done building path") 

    def start_moving(self, index):

        path_copy = self.list_paths[index]
        self.model.set_path(path_copy)
        print("Start moving")
        i = 0
        while (path_copy.get_path()):
            print("Updated" + str(i) + " times")
            path_copy.update_current_instruction()
            current_instruction = path_copy.get_current_instruction()
            instruction_speed = current_instruction.get_speed()
            instruction_angle = current_instruction.get_angle()
            if (current_instruction.get_action() == 0):
                self.model.moveForward(instruction_speed)
                self.model.turnLeft(instruction_angle)
            elif (current_instruction.get_action() == 1):
                self.model.moveForward(instruction_speed)
                self.model.turnRight(instruction_angle)
            elif (current_instruction.get_action() == 2):
                self.model.moveBackward(instruction_speed)
                self.model.turnLeft(instruction_angle)
            elif (current_instruction.get_action() ==3):
                self.model.moveBackward(instruction_speed)
                self.model.turnRight(instruction_angle)
            elif (current_instruction.get_action() == 4):
                self.model.moveForward(instruction_speed)
            elif (current_instruction.get_action() == 5):
                self.model.moveBackward(instruction_speed)
            else:
                print ("ERROR: Impossible to retrieve the informations of the current instruction")
                     
            i = i+1     




    
