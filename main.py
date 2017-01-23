#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""
     The main module
     ===============
"""

import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from Controllers import window, StmController, preloadedPath, checkDistance, camera, detect_obstacle
from Model.car import Car
from Model.world import World
from pygame import mixer
import time 

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
        self.cam = camera.Camera(model)
        self.check_distance = checkDistance.CheckDistance(model)
        self.detect_obstacle = detect_obstacle.DetectObstacle(model)
        self.window = window.Window(model, self.preloadedPaths)
        self.window.show()
        
        mixer.init()
        mixer.music.load('little_helper.mp3')
        mixer.music.set_volume(1.0)
        mixer.music.play()

#        time.sleep(5)

        # Start the different threads
        self.spi.start()
        self.preloadedPaths.start()
        self.cam.start()
        self.check_distance.start()
        self.detect_obstacle.start()

        sys.exit(app.exec_())


    def cleanUp(self):
        self.window.stop()
        print("window closed")
        self.spi.stop()
        self.preloadedPaths.stop()
        self.cam.stop()
        self.check_distance.stop()
        self.detect_obstacle.stop()
        print("close ok")

def main():

    """
         The function starting the application
    """


    miles = MilesApp()
    print("close ok")

if __name__ == "__main__":

    main()
