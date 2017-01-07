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
from multiprocessing.managers import BaseManager, NamespaceProxy

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

        BaseManager.register('Model', World, Proxy)
        manager = BaseManager()
        manager.start()
        self.model = manager.Model(self.car)

        # self.model = World(self.car)
        self.preloadedPaths = preloadedPath.PreloadedPaths(self.model)
        self.spi = StmController.StmController(self.model)
        self.window = window.Window(self.model, self.preloadedPaths)
        self.window.show()
        self.spi.start()
#        self.preloadedPaths.start()

    def cleanUp(self):
        self.window.stop()
        print("window closed")
        #self.spi.stop()

class Proxy(NamespaceProxy):
    # We need to expose the same __dunder__ methods as NamespaceProxy
    _exposed_ = ('__getattribute__', '__setattr__', '__delattr__')

def main():

    """
         The function starting the application
    """

    app = QApplication(sys.argv)
    miles = MilesApp(app)
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()

# exemple du multi processing

# from multiprocessing import Process
# from multiprocessing.managers import BaseManager, NamespaceProxy
# import sys
# import time
#
# class Model(object):
#     def __init__(self):
#         self.__speed = 0
#         self.__distance = 0
#
#     @property
#     def distance(self):
#         return self.__distance
#     @distance.setter
#     def distance(self, value):
#         self.__distance = value
#     @property
#     def speed(self):
#         return self.__speed
#     @speed.setter
#     def speed(self, value):
#         self.__speed = value
#
# class Path(Process):
#     def __init__(self, model):
#         Process.__init__(self)
#         self.model = model
#
#     def run(self):
#         for i in range(10):
#             print("Path : " + (str(self.model.distance) + " - " +str(self.model.speed)))
#             sys.stdout.flush()
#
#
# class Spi(Process):
#     def __init__(self, model):
#         Process.__init__(self)
#         self.model = model
#
#     def run(self):
#         for i in range(10):
#             print("Spi : " + (str(self.model.distance) + " - " +str(self.model.speed)))
#             sys.stdout.flush()
#
# class Proxy(NamespaceProxy):
#     # We need to expose the same __dunder__ methods as NamespaceProxy
#     _exposed_ = ('__getattribute__', '__setattr__', '__delattr__')
#
#
# if __name__ == '__main__':
#     BaseManager.register('Model', Model, Proxy)
#     manager = BaseManager()
#     manager.start()
#     model = manager.Model()
#
#     path = Path(model)
#     path.start()
#
#     spi = Spi(model)
#     spi.start()
#
#     for i in range(10):
#         model.distance = i
#         model.speed = i
#         sys.stdout.flush()
#
#
#
#     path.join()
#     spi.join()
