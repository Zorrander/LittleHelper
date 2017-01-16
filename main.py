#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""
     The main module
     ===============
"""

import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from Controllers import window, StmController, preloadedPath, checkDistance #, camera
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

    def __init__(self):
        app = QApplication(sys.argv)

        app.aboutToQuit.connect(self.cleanUp)

        # initialisation
        car = Car()
        model = World(car)
        self.preloadedPaths = preloadedPath.PreloadedPaths(model)
        self.spi = StmController.StmController(model)

        self.window = window.Window(model, self.preloadedPaths)
        self.window.show()

        # Start the different threads
        self.spi.start()
        self.preloadedPaths.start()

        sys.exit(app.exec_())


    def cleanUp(self):
        self.window.stop()
        print("window closed")
        self.spi.stop()
        self.preloadedPaths.stop()
        #spi.join()
        #preloaded.join()
        print("close ok")

def main():

    """
         The function starting the application
    """


    miles = MilesApp()


    print("close ok")

if __name__ == "__main__":

    main()
