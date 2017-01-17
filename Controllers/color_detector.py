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
    roadDetect = ColorFilter()
    img = cv2.imread('../img/road.jpg')
    img = cv2.resize(img, (640, 480))
    img = cv2.blur(img, (10, 10))
    roadDetect.img = img
    roadDetect.process()
    roadDetect.display()
    cv2.waitKey(0)
