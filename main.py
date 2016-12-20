#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
     The main module
     ===============
"""

import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from Controllers import window, StmController, preloadedPath
from Model.car import Car
from Model.world import World




class MilesApp():

    """
        The MilesApp class
        ------------------

        Caracteristics:
            >>> 3 attributs

        This is the main class initializing the model and the controllers. Architecture MVC.

    """

    def __init__(self, instance):
        self.app = instance
        instance.aboutToQuit.connect(self.cleanUp)
        self.car = Car()
        self.model = World(car)
        self.preloadedPaths = preloadedPath.PreloadedPaths(self.model)
        self.spi = StmController.StmController(self.model)
        self.window = window.Window(self.model, self.preloadedPaths)
        self.window.show()
        self.spi.start()
        self.preloadedPaths.start()

    def cleanUp(self):
        self.window.stop()
        print("window closed")
        #self.spi.stop()

def main():

    """
         The function starting the application
    """

    app = QApplication(sys.argv)
    miles = MilesApp(app)
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
