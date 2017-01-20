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
        Used to manage the current path followed by the car

        Caracteristics :
            >>> a list of instructions
    """

    def __init__(self):
        # list of instructions corresponding to the path
        self.instructions_list = []

    def add_instruction(self, instruction):
        """
            Used to add an instruction to the path.
            The instruction is add at the end of the path.

            :param instruction: The instruction to add
            :type instruction: Instruction
        """
        self.instructions_list.append(instruction)

    def del_first_instruction(self):
        """
            Used to delete the first instruction of the list of instruction
        """
        del self.instructions_list[0]

    def get_path(self):
        """
            The path of the car

            :getter: Returns the list of instructions
            :type: Instruction[]
        """
        return self.instructions_list

    def get_current_instruction(self):
        """
            The current instruction of the path

            :getter: Returns the first element of the list of instructions
            :type: Instruction
        """
        return self.instructions_list[0]

class Paths():
    """
        Used to build and save the differents path available.

        Caracteristics :
            >>> a list of paths
    """

    def __init__(self):
        self.paths = []
        self.build_paths()

    def build_paths(self):
        """
            Create the differents paths of the car and save them in the list of paths.
        """
        # ====================================================================
        #                      Creation of the first path
        # ====================================================================
        path = Path()
        path.add_instruction(Instruction(FORWARD, speed=40, distance=100))
        path.add_instruction(Instruction(FORWARD, speed=40, distance=100))
        path.add_instruction(Instruction(FORWARD, speed=40, distance=100))
        path.add_instruction(Instruction(FORWARD, speed=40, distance=100))
#        path.add_instruction(Instruction(TURN_LEFT))
        path.add_instruction(Instruction(FORWARD, speed=40, distance=100))
        path.add_instruction(Instruction(FORWARD, speed=40, distance=100))
        path.add_instruction(Instruction(FORWARD, speed=40, distance=100))

        path.add_instruction(Instruction(STOP, sleep_time=5))

        self.paths.append(path)

        # ====================================================================
        #                      Creation of the first path
        # ====================================================================
        path = Path()
        path.add_instruction(Instruction(FORWARD, speed=40, distance=100))
        path.add_instruction(Instruction(FORWARD, speed=40, distance=100))
        path.add_instruction(Instruction(FORWARD, speed=40, distance=100))
        path.add_instruction(Instruction(FORWARD, speed=40, distance=100))
        path.add_instruction(Instruction(TURN_RIGHT))
        path.add_instruction(Instruction(STOP, sleep_time=5))

        self.paths.append(path)

    def get_path(self, index):
        """
            Return the path corresponding to the index.

            :param index: The index of the path asked
            :type index: int

            :getter: Returns the path corresponding to the index number
            :type: Path
        """
        return copy(self.paths[index])
