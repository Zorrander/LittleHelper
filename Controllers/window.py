#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The window module
    =================

    Used to handle the communication between the user and the RaspberryPi.

"""

import sys
import PyQt5
#import cv2
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, Qt
import GUI.mainwindow_auto
from Model import car
from Observer import observer
#import video
import preloadedPath



class Window(QMainWindow, GUI.mainwindow_auto.Ui_MainWindow, observer.Observer):



    def __init__(self, model, preloadPath):

        observer.Observer.__init__(self, model)
        super(self.__class__, self).__init__()
        self.model = model
        self.ui = GUI.mainwindow_auto.Ui_MainWindow()
        self.ui.setupUi(self)
	self.preloadPath = preloadPath
        # Video
        #self.video = video.Video(cv2.VideoCapture(0))
        #self.timer = QtCore.QTimer(self)
        #self.timer.timeout.connect(self.play)
        #self.timer.start(27)
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


    def stop(self):
        self.timer.stop()
        self.video.stop()
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

        ////!!!!!\\\\\
        NEED TO BE MODIFIED TO TAKE INTO ACCOUNT ALL THE SENSORS
        ////!!!!!\\\\\
        """
        distance = sensor.getDist()
        if (distance < 40):
            self.ui.us_ar.setText(str(distance))
            self.ui.us_ar.setStyleSheet("background-color:red;")
        elif (distance < 80):
            self.ui.us_ar.setText(str(distance))
            self.ui.us_ar.setStyleSheet("background-color:orange;")
        elif (distance < 180):
            self.ui.us_ar.setText(str(distance))
            self.ui.us_ar.setStyleSheet("background-color:green;")
        elif (distance > 300):
            print("POTENTIAL ERROR")


    def update(self):
        for sensor in self.model.sensors:
            self.checkSensor(sensor)


    def pressedMyPathsButton(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def pressedCmdButton(self):
        self.ui.tabWidget.setCurrentIndex(2)

    def pressedOverviewButton(self):
        self.ui.tabWidget.setCurrentIndex(3)

    def pressedMotorsButton(self):
        self.ui.tabWidget.setCurrentIndex(4)

    def pressedSensorsButton(self):
        self.ui.tabWidget.setCurrentIndex(5)

    def pressedForwardButton(self):
        self.model.moveForward(20)

    def pressedBackwardButton(self):
        self.model.moveBackward(20)

    def pressedStopButton(self):
        self.model.stop()

    def pressedLeftButton(self): 
        self.model.turnLeft(30)

    def pressedRightButton(self):
        self.model.turnRight(30)

    def pressedPathButton(self):
        self.preloadPath.start_path(0)


