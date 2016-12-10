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
from PyQt5.QtCore import pyqtSignal, pyqtSlot


class Window(QMainWindow, GUI.mainwindow_auto.Ui_MainWindow, observer.Observer):

    update = pyqtSignal()


    def __init__(self, model, preloadPath):

        observer.Observer.__init__(self, model)
        super(self.__class__, self).__init__()
        self.model = model
        self.ui = GUI.mainwindow_auto.Ui_MainWindow()
        self.ui.setupUi(self)  
	self.preloadPath = preloadPath  
#        self.update.connect(self.checkSensor)

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

    def processId(self, sensor, distance):
        id = sensor.getId()
        if id == 0:
            self.ui.us_av.setText(str(distance))
        if id == 1:
            self.ui.us_av_g.setText(str(distance))
        if id == 2:
            self.ui.us_av_d.setText(str(distance))
        if id == 3:
            self.ui.us_ar.setText(str(distance))
        if id == 4:
            self.ui.us_ar_g.setText(str(distance))
        if id == 5:
            self.ui.us_ar_d.setText(str(distance))

    @pyqtSlot()
    def checkSensor(self):
        """
        Perform analysis on the sensor before displaying on the RasPi
        """ 
        for sensor in self.model.sensors: 
            distance = sensor.getDist()
            print("Got a distance of " + str(distance))
            sensor = self.processId(sensor, distance)


    def update(self):
        self.update.emit()

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


