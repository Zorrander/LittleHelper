#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The video module
    =================

    Used to handle the frames retrieved via the camera.

"""

import sys
import PyQt5
from PyQt5 import QtGui
import cv2
import numpy as np
import GUI.mainwindow_auto

class Video():



    def __init__(self,capture):
        self.capture = capture
        self.currentFrame = np.array([])
        self.fgmask = np.array([])
        self.fgbg = cv2.BackgroundSubtractorMOG()

    def captureNextFrame(self):
        ret, readFrame = self.capture.read()
        if(ret == True):
            self.currentFrame=cv2.cvtColor(readFrame,cv2.COLOR_BGR2RGB)

    def convertFrame(self, picture, format):
        try:
            height,width = self.currentFrame.shape[:2]
            img = QtGui.QImage(picture, width, height, format)
            img = QtGui.QPixmap.fromImage(img)
            return img
        except:
            return None

    def turnBlackAndWhite(self, picture):
        return cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY)

    def blur(self, picture):
        return cv2.GaussianBlur(picture, (21, 21), 0)


    def detectEdges(self):
        try:
            gray_version = self.turnBlackAndWhite(self.currentFrame)
            edges = cv2.Canny(gray_version, 100, 200)
            return edges
        except:
            return None

    def backgroundSubstraction(self):
        try :
            self.fgmask = self.fgbg.apply(self.currentFrame,learningRate=0.1)
            return self.fgmask
        except:
             return None

    def displayCamera(self, window):
        window.videoFrame.setPixmap(self.convertFrame(self.currentFrame, QtGui.QImage.Format_RGB888))
        window.videoFrame.setScaledContents(True)


    def displayEdgeDetection(self, window):
        window.computedVideoFrame.setPixmap(self.convertFrame(self.detectEdges(), QtGui.QImage.Format_Indexed8))
        window.computedVideoFrame.setScaledContents(True)


    def displayBackgroundSubstraction(self, window):
        window.computedVideoFrame.setPixmap(self.convertFrame(self.backgroundSubstraction(), QtGui.QImage.Format_Indexed8))
        window.computedVideoFrame.setScaledContents(True)



    def stop(self):
        self.capture.release()
