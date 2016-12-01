#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The window module
    =================

    Used to handle the communication between the user and the RaspberryPi.

"""

import sys
import PyQt5
import cv2
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, Qt
import GUI.mainwindow_auto
from Model import car
from Observer import observer
from . import preloadedPath


class Video():

    def __init__(self,capture):
        self.capture = capture
        self.currentFrame = np.array([])

    def captureNextFrame(self):
        ret, readFrame = self.capture.read()
        if(ret == True):
            self.currentFrame=cv2.cvtColor(readFrame,cv2.COLOR_BGR2RGB)


    def convertFrame(self):
        try:
            height,width = self.currentFrame.shape[:2]
            img = QtGui.QImage(self.currentFrame, width, height, QtGui.QImage.Format_RGB888)
            img = QtGui.QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None

class Window(QMainWindow, GUI.mainwindow_auto.Ui_MainWindow, observer.Observer):

    def __init__(self, model, preloadPath):

        observer.Observer.__init__(self, model)
        super(self.__class__, self).__init__()
        self.model = model
        self.ui = GUI.mainwindow_auto.Ui_MainWindow()
        self.ui.setupUi(self)

        # Video
        self.video = Video(cv2.VideoCapture(0))
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.play)
        self.timer.start(27)
        self.update()
        # go!
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

    def play(self):
           try:
               self.video.captureNextFrame()
               self.ui.videoFrame.setPixmap(self.video.convertFrame())
               self.ui.videoFrame.setScaledContents(True)
           except TypeError:
               print ("No frame")


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
        self.preloadPath.start_moving(0)


