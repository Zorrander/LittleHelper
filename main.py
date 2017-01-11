#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
     The main module
     ===============
"""

import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from Controllers import window, StmController, preloadedPath, checkDistance, camera
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

        # initialisation
        self.car = Car()
        self.model = World(self.car)
        self.preloadedPaths = preloadedPath.PreloadedPaths(self.model)
        self.spi = StmController.StmController(self.model)
        self.cam = camera.Camera(self.model)
        # TODO:
        band_xcoord = 0
        # end TODO:
        self.checkDistance = checkDistance.CheckDistance(self.model, band_xcoord, sema_band_xcoord)
        self.window = window.Window(self.model, self.preloadedPaths)
        self.window.show()

        # Start the different threads
        self.spi.start()
        self.preloadedPaths.start()
        self.cam.start()
        #self.checkDistance.start()

    def cleanUp(self):
        self.window.stop()
        print("window closed")

def main():

    """
         The function starting the application
    """

    app = QApplication(sys.argv)
    miles = MilesApp(app)
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
