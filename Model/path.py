#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The path module
    ===============
    Used to represent the path

"""

from copy import copy
from instructions import Instruction
from constant import FORWARD, BACKWARD, STOP, TURN_LEFT, TURN_RIGHT

class Path():

    """
        The path class
        --------------

    """

    def __init__(self):
        # list of instructions corresponding to the path
        self.instructions_list = []

    def add_instruction(self, instruction):
        self.instructions_list.append(instruction)

    def del_first_instruction(self):
        del self.instructions_list[0]

    def get_path(self):
        return self.instructions_list

    def get_current_instruction(self):
        return self.instructions_list[0]

class Paths():
    """
        The paths class
        --------------
    """

    def __init__(self):
        self.paths = []
        self.build_paths()

    def build_paths(self):
        # ====================================================================
        #                      Creation of the first path
        # ====================================================================
        path = Path()
        path.add_instruction(Instruction(FORWARD, speed=35, distance=100))
        path.add_instruction(Instruction(FORWARD, speed=35, distance=50))
        path.add_instruction(Instruction(TURN_LEFT))
        path.add_instruction(Instruction(STOP, sleep_time=5))

        self.paths.append(path)

    def get_path(self, index):
        return copy(self.paths[index])
