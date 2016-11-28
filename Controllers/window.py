#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The window module
    =================

    Used to handle the communication between the user and the RaspberryPi.

"""

import sys
import PyQt5
from PyQt5.QtWidgets import *
import GUI.mainwindow_auto
from Model import car
from Observer import observer


class Window(QMainWindow, GUI.mainwindow_auto.Ui_MainWindow, observer.Observer):

    def __init__(self, model):

        observer.Observer.__init__(self, model)
        super(self.__class__, self).__init__()
        self.model = model
        self.setupUi(self)
        # go!
        self.myPathsButton.clicked.connect(lambda: self.pressedMyPathsButton())
        self.cmdButton.clicked.connect(lambda: self.pressedCmdButton())
        self.overviewButton.clicked.connect(lambda: self.pressedOverviewButton())
        self.motorsButton.clicked.connect(lambda: self.pressedMotorsButton())
        self.sensorsButton.clicked.connect(lambda: self.pressedSensorsButton())
        self.forwardButton.clicked.connect(lambda: self.pressedForwardButton())
        self.backwardButton.clicked.connect(lambda: self.pressedBackwardButton())
        self.stopButton.clicked.connect(lambda: self.pressedStopButton())
        self.leftButton.clicked.connect(lambda: self.pressedLeftButton())
        self.rightButton.clicked.connect(lambda: self.pressedRightButton())

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
        self.model.moveForward

    def pressedBackwardButton(self):
        self.model.moveBackward

    def pressedStopButton(self):
        self.model.stop

    def pressedLeftButton(self):
        self.model.turnLeft

    def pressedRightButton(self):
        self.model.turnRight



