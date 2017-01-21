#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The color detector module
    =========================

    Used to manage the detection of the color of the road.
"""
import cv2
import numpy as np


class ColorFilter:
    """
        This class provides a simple method for color filtering based on the HSV color space, the image sample needs to be
        blurred before being passed to this filter
    """

    DEFAULT_COLOR_THRESHOLDS = [np.array([0, 0, 20]), np.array([200, 40, 200])]   # kinda gray, for road detection

    def __init__(self):
        """
            Class constructor, set all attributes to their default values
        """
        self.__img = None
        self.__mask = None
        self.__colorThresholds = ColorFilter.DEFAULT_COLOR_THRESHOLDS

    def set_thresholds(self, thresh):
        self.__colorThresholds = thresh

    @property
    def color_thresholds(self):
        """
            :getter: Gets the lower and upper threshold for color filtering
            :type: array of two numpy arrays
        """
        return self.__colorThresholds

    @color_thresholds.setter
    def color_thresholds(self, thresholds):
        """
            :setter: Sets the lower and upper threshold for color filtering
            :type: array of two numpy arrays
        """
        self.__colorThresholds = thresholds

    @property
    def img(self):
        """
            :getter: Gets the image before filtered
            :type:
        """
        return self.__img

    @property
    def mask(self):
        """
            :getter: Gets the mask after processing
            :type:
        """
        return self.__mask

    def process(self):
        """
            Start processing
        """
        try:
            hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
            self.__mask = cv2.inRange(hsv, self.__colorThresholds[0], self.__colorThresholds[1])
        except cv2.error:
            print("process: image not found!!!")

    def display(self, raw_img=True):
        """
            Display the mask and the raw image
            :param raw_img: if True, the raw image will be displayed
            :type raw_img: boolean
        """
        cv2.imshow('mask', self.__mask)
        if raw_img:
            cv2.imshow('raw image', self.__img)


if __name__ == '__main__':
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    from constant import *
    import time

    # init camera
    camera = PiCamera()
    camera.resolution = (640,480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640,480))

    #
    roadDetect = ColorFilter()
    roadDetect.set_thresholds([np.array([100, 20, 0]), np.array([140, 255, 255])])

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        img = frame.array
        img = cv2.blur(img, (10, 10))
        cv2.imshow('hsv', cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
        roadDetect.img = img
        roadDetect.process()
        roadDetect.display(raw_img=False)

        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        if key == ord("q"):
            break
