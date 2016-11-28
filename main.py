#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
     The main module
     ===============
"""

import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from Controllers import window, StmController
from Model import car



def singleton(classe):

    """
        This will be used to ensure the unicity of the instance of our application
    """

    instances = {}
    def get_instance():
        if classe not in instances:
            instances[classe] = classe()
        return instances[classe]
    return get_instance


@singleton
class MilesApp():

    """
        The MilesApp class
        ------------------

        Caracteristics:
            >>> 3 attributs

        This is the main class initializing the model and the controllers. Architecture MVC.

    """

    def __init__(self):
        self.model = car.Car()
        self.spi = StmController.StmController(self.model)
        self.window = window.Window(self.model)
        self.window.show()




def main():

    """
         The function starting the application
    """

    app = QApplication(sys.argv)
    miles = MilesApp()

    sys.exit(app.exec_())

if __name__ == "__main__":

    main()
