#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The path module
    ===============
    Used to represent the path

"""

from copy import copy
from instructions import Instruction
from constant import FORWARD, BACKWARD, STOP, LEFT, RIGHT

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
        # creation of the instructions
        inst1 = Instruction(FORWARD, LEFT, 35, 0, 200, 0)
        inst2 = Instruction(FORWARD, LEFT, 35, 40, 150, 0)
        inst3 = Instruction(FORWARD, LEFT, 35, 0, 100, 0)
        inst4 = Instruction(STOP, LEFT, 0, 0, 0, 5)

        # creation of the path
        path = Path()
        path.add_instruction(inst1)
        path.add_instruction(inst2)
        path.add_instruction(inst3)
        path.add_instruction(inst4)

        self.paths.append(path)

    def get_path(self, index):
        return copy(self.paths[index])
