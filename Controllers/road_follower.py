#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The road follower module
    ========================

    Used to manage the car to stay in the center of the road

"""

import color_detector as cd
import cv2
import numpy as np
import math
from constant import *


class RoadFollower:
    """
    The class RoadFollower contains:
    >>> Two members which are instances of ColorFilter
    >>> Two color thresholds which correspond to the color filters above
    >>> A proportional gain for regulation system
    >>> An angle for the car to follow
    """
    # frame's factors
    __IMG_SIZE = (640, 480)
    __BLUR_K_SIZE = (10, 10)
    # horizontal window crop
    __HW_X1 = 0
    __HW_X2 = __IMG_SIZE[0]
    __HW_Y1 = 150
    __HW_Y2 = __HW_Y1 + 80
    # vertical window crop
    __VW_X1 = int(__IMG_SIZE[0] / 2 - 70)
    __VW_X2 = __VW_X1 + 140
    __VW_Y1 = 100
    __VW_Y2 = __VW_Y1 + 250

    # default prop factor
    __Kp = 0.0015

    # minimum size for strip detection
    __STRIP_MIN_SIZE = (50 * 50)

    def __init__(self):
        """
            Constructor, initialize color thresholds for blue and gray filtering
        """
        self.__colorDetectV = cd.ColorFilter()
        self.__colorDetectH = cd.ColorFilter()
        self.__colorDetectV.color_thresholds = [LOWER_BLUE, UPPER_BLUE]
        self.__colorDetectH.color_thresholds = [LOWER_GRAY, UPPER_GRAY]
        self.__kp = RoadFollower.__Kp
        self.__angle = 0

    def update_frame(self, image):
        """
            Update the current frame for processing
            :param image: the current frame to be updated
            :type image: numpy array
        """
        try:
            if image.shape[0] != RoadFollower.__IMG_SIZE[1] or image.shape[1] != RoadFollower.__IMG_SIZE[0]:
                image = cv2.resize(image, RoadFollower.__IMG_SIZE)
            image = cv2.blur(image, RoadFollower.__BLUR_K_SIZE)
            self.__colorDetectH.img = image[RoadFollower.__HW_Y1:RoadFollower.__HW_Y2,
                                            RoadFollower.__HW_X1:RoadFollower.__HW_X2]
            self.__colorDetectV.img = image[RoadFollower.__VW_Y1:RoadFollower.__VW_Y2,
                                            RoadFollower.__VW_X1:RoadFollower.__VW_X2]
        except AttributeError:
            print("update_frame: Can't update, frame not found!!!")

    def set_thresholds(self, v_thresh, h_thresh):
        """
            Set the thresholds for other color filtering
            :param v_thresh: thresholds for vertical window
            :type v_thresh: list of two numpy array, for lower and upper thresholds
            :param h_thresh: thresholds for horizontal window
            :type h_thresh: list of two numpy array, for lower and upper thresholds
        """
        self.__colorDetectV.color_thresholds = v_thresh
        self.__colorDetectH.color_thresholds = h_thresh

    def filter(self):
        """
            Start filtering
        """
        try:
            self.__colorDetectV.process()
            self.__colorDetectH.process()
        except cv2.error:
            print("filter: Can't process, image not found!!!")

    def compute_deviation(self):
        """
            Calculate the angle for the car to follow
            :return: the angle to follow
            :rtype: int
        """
        try:
            non_zeros_left = cv2.countNonZero(self.__colorDetectH.mask[:, 0:320])
            non_zeros_right = cv2.countNonZero(self.__colorDetectH.mask[:, 320:640])
            delta = non_zeros_right - non_zeros_left
            self.__angle = int(delta * self.__kp / (1.0 - self.__kp))
            if self.__angle <= -45:
                self.__angle = -45
            elif self.__angle >= 45:
                self.__angle = 45
            return self.__angle
        except TypeError:
            print("compute_deviation: Can't compute, image not found!!!")
            self.__angle = 0

    def compute_strip_position(self):
        """
            Compute the position of strip
            :return: the coordonation (y only) of the strip's center
            :rtype: int
        """
        _, contours, _ = cv2.findContours(self.__colorDetectV.mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cx, cy = 0
        if len(contours) != 0:
            for i in range(len(contours)):
                moment = cv2.moments(contours[i])
                if moment['m00'] > RoadFollower.__STRIP_MIN_SIZE:
                    cx = int(moment['m10'] / moment['m00'])
                    cy = int(moment['m01'] / moment['m00'])
                    break
        return cy

    def display_masks(self):
        """
            Display masked images, for debugging only
        """
        try:
            cv2.imshow('mask V', self.__colorDetectV.mask)
            cv2.imshow('mask H', self.__colorDetectH.mask)
        except cv2.error:
            print("display_masks: Can't display, image not found!!!")


if __name__ == '__main__':

    road_follow = RoadFollower()
    cap = cv2.VideoCapture("../video/MOV_0304.mp4")
    simulation = np.zeros((200,  400, 3), np.uint8)

    while cap.isOpened():
        ret, frame = cap.read()
        if frame is None:
            break
        frame = cv2.resize(frame, (640, 480))
        cv2.imshow("frame", frame)
        road_follow.update_frame(frame)
        road_follow.filter()
        road_follow.display_masks()
        print(int(road_follow.compute_deviation()))
        alpha = road_follow.compute_deviation()
        if not 45.0 >= alpha >= -45.0:
            alpha = 45.0
        point_a = (200, 150)
        point_b = (int(200 + 100 * math.tan(math.radians(alpha))), 50)
        cv2.line(simulation, point_a, point_b, (255, 0, 0), thickness=5)
        cv2.imshow("sim", simulation)
        simulation = np.zeros((200, 400, 3), np.uint8)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
