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
import time

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
#        self.thread = threading.Thread(target=self.start_moving, args=())
#        self.thread.start() 

    def build_list(self):
    
        #instructions.Instruction(action, speed, angle, distance, sleep_time):
        forward = 0
        backward = 1
        left = 2
        right = 3
        stop = 4
        
        # move 
        instruct_move1 = instructions.Instruction(forward, 35, 0, 100, 0) 
        instruct_move2 = instructions.Instruction(forward, 35, 0, 200, 0) 
        # move fast
        instruct_move_fast = instructions.Instruction(forward, 75, 0, 150, 0)
        # stop
        instruct_stop = instructions.Instruction(stop, 0, 0, 0, 5)
        # turn left
        instruct_turn_left = instructions.Instruction(left, 0, 40, 0, 0)
        # turn right
        instruct_turn_right = instructions.Instruction(right, 0, 40, 0, 0)

        new_path = path.Path()
        new_path.add_instruction(instruct_move1)
        new_path.add_instruction(instruct_move_fast)
        new_path.add_instruction(instruct_turn_right)
        new_path.add_instruction(instruct_stop)
        new_path.add_instruction(instruct_move2)
        new_path.add_instruction(instruct_stop)
      
        self.list_paths.append(new_path)
        print("Done building path") 

    def start_path(self, index):
  
        self.path_copy = self.list_paths[index]
        self.model.set_path(self.path_copy)
        self.start_moving()     

    def start_moving(self):
#        while(1):	
           # if (len(self.path_copy.get_path()) != 0):
            while (len(self.path_copy.get_path()) != 0):
                current_instruction = self.path_copy.get_current_instruction()
                
                # forward
                if (current_instruction.get_action() == 0):
                    instruction_speed = current_instruction.get_speed()                
                    self.model.moveForward(instruction_speed)
                    self.model.turnRight(0)
                    if(current_instruction.get_distance() <= self.path_copy.get_current_distance()):
                        self.path_copy.del_first_instruction() 

                # backward
                elif (current_instruction.get_action() == 1):
                    instruction_speed = current_instruction.get_speed()        
                    self.model.moveBackward(instruction_speed)
                    self.model.turnRight(0)
                    if(current_instruction.get_distance() <= self.path_copy.get_current_distance()):
                        self.path_copy.del_first_instruction() 

                # left
                elif (current_instruction.get_action() == 2):
                    # we stop the car before turning
                    self.model.moveForward(0)
                    instruction_angle = current_instruction.get_angle()
                    self.model.turnLeft(instruction_angle)
                    # we update the position of the car 
                    self.model.update_angle(instruction_angle)
                    # We go on to the next action
                    self.path_copy.del_first_instruction() 

                # right 
                elif (current_instruction.get_action() ==3):
                    # we stop the car before turning
                    self.model.moveForward(0)
                    instruction_angle = current_instruction.get_angle()
                    self.model.turnRight(instruction_angle)
                    # we update the position of the car 
                    self.model.update_angle(-instruction_angle)
                    # We go on to the next action
                    self.path_copy.del_first_instruction() 

                # stop 
                elif (current_instruction.get_action() == 4):
                    self.model.moveForward(0)
                    time_sleep = current_instruction.get_sleep_time()
                    print("deb of sleep")
                    time.sleep(time_sleep)
                    print("end of sleep")
                    # We go on to the next action
                    self.path_copy.del_first_instruction() 
                else:
                    print ("ERROR: Impossible to retrieve the informations of the current instruction")



    
