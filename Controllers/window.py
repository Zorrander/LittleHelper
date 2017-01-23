#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The window module
    =================

    Used to handle the communication between the user and the RaspberryPi.

"""
import os
import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, Qt
import GUI.mainwindow_auto
from Model import car

import preloadedPath

class Window(QMainWindow, GUI.mainwindow_auto.Ui_MainWindow):
    """
        Initialize the GUI and connect all the buttons

    """
    def __init__(self, model, preloadPath):
        super(self.__class__, self).__init__()

        self.model = model
        self.preloadPath = preloadPath
        self.ui = GUI.mainwindow_auto.Ui_MainWindow()
        self.ui.setupUi(self)

        # Buttons
        self.ui.myPathsButton.clicked.connect(lambda: self.pressedMyPathsButton())
        self.ui.cmdButton.clicked.connect(lambda: self.pressedCmdButton())
        self.ui.overviewButton.clicked.connect(lambda: self.pressedOverviewButton())
        self.ui.motorsButton.clicked.connect(lambda: self.pressedMotorsButton())
        self.ui.sensorsButton.clicked.connect(lambda: self.pressedSensorsButton())
        self.ui.forwardButton.clicked.connect(lambda: self.pressedForwardButton())
        self.ui.backwardButton.clicked.connect(lambda: self.pressedBackwardButton())
        self.ui.stopButton.clicked.connect(lambda: self.pressedStopButton())
        self.ui.leftButton.clicked.connect(lambda: self.pressedLeftButton())
        self.ui.rightButton.clicked.connect(lambda: self.pressedRightButton())
        self.ui.pathButton.clicked.connect(lambda: self.pressedPathButton())
        self.ui.pathButton_2.clicked.connect(lambda: self.pressedPathButton2())
        self.ui.pathButton_3.clicked.connect(lambda: self.pressedPathButton3())
        self.ui.changeButton.clicked.connect(lambda: self.pressedChangeButton())

    def pressedChangeButton(self):
        self.model.changeValues()

    def stop(self):
        self.close()

    def play(self):
           try:
               self.video.captureNextFrame()
               self.video.displayCamera(self.ui)
               #self.video.displayEdgeDetection(self.ui)
               self.video.displayBackgroundSubstraction(self.ui)
           except TypeError:
               print ("No frame")

    def checkSensor(self, sensor):
        """
            Perform analysis on the sensor before displaying on the RasPi
        """
        dist = sensor.getDist()
        print("==========DATA SENSORS===========")
        print("SENSOR " + sensor.getName() + " >>> " + str(dist) )
        if (dist < 45):
            print("STATE >>> RED ")
        elif(dist < 80):
            print("STATE >>> ORANGE")
        elif(dist < 250):
            print("STATE >>> GREEN")
        else:
            print("STATE >>> BLUE")

    def update(self):
        os.system('clear')
        for sensor in self.model.sensors:
            self.checkSensor(sensor)

    def pressedMyPathsButton(self):
        self.tabWidget.setCurrentIndex(1)

    def pressedCmdButton(self):
        self.tabWidget.setCurrentIndex(2)

    def pressedOverviewButton(self):
        self.tabWidget.setCurrentIndex(3)

    def pressedMotorsButton(self):
        self.tabWidget.setCurrentIndex(4)

    def pressedSensorsButton(self):
        self.tabWidget.setCurrentIndex(5)

    def pressedForwardButton(self):
        self.model.car.moveForward(50)

    def pressedBackwardButton(self):
        self.model.car.moveBackward(50)

    def pressedStopButton(self):
        self.model.car.stop()
        self.preloadPath.stop_path()

    def pressedLeftButton(self):
        self.model.car.turnLeft(40)

    def pressedRightButton(self):
        self.model.car.turnRight(40)

    def pressedPathButton(self):
        self.preloadPath.start_path(0)

    def pressedPathButton2(self):
        self.preloadPath.start_path(1)

    def pressedPathButton3(self):
        self.preloadPath.start_path(2)
