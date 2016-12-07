
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The PreloadedPaths module
    =========================

    Used to represent the list of paths
    
"""
from Model import path
from Model import instructions
import threading 

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
        self.path_copy = path.Path()
        self.thread = threading.Thread(target=self.start_moving, args=())
        self.thread.start() 

    def build_list(self):
        forward_left = 0
        forward_right = 1 
        backward_left = 2
        backward_right = 3
        forward = 4
        backward = 5
        instruct_move = instructions.Instruction(forward, 35, 0, 100) 
        instruct_move_fast = instructions.Instruction(forward, 75, 0, 200)
        instruct_stop = instructions.Instruction(forward, 0, 0, 200)
        instruct_turn_left = instructions.Instruction(forward_left, 35, 40, 150)
        instruct_turn_right = instructions.Instruction(forward_right, 35, 40, 200)

        new_path = path.Path()
        new_path.add_instruction(instruct_move)
#        new_path.add_instruction(instruct_move_fast)
#        new_path.add_instruction(instruct_stop)
        new_path.add_instruction(instruct_turn_left)
        new_path.add_instruction(instruct_turn_right)
#        new_path.add_instruction(instruct_stop)
      
        self.list_paths.append(new_path)
        print("Done building path") 


       	sleep_mode = path.Path()
      	self.list_paths.append(sleep_mode)

    def start_path(self, index):
        self.path_copy = self.list_paths[index]
        self.model.set_path(self.path_copy)
      

    def start_moving(self):
       while(1):	
           if (len(self.path_copy.get_path()) != 0):
               current_instruction = self.path_copy.get_current_instruction()
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
                   self.model.turnRight(0)
               elif (current_instruction.get_action() == 5):
                   self.model.moveBackward(instruction_speed)
                   self.model.turnRight(0)
               else:
                   print ("ERROR: Impossible to retrieve the informations of the current instruction")
                    
               self.path_copy.update_current_instruction()




    
