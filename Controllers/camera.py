#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The camera module
    =================

    Used to manage the camera

"""

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from road_follower import RoadFollower
from threading import Thread
from constant import *
import time
import cv2

class Camera(Thread):
    """
        The camera is composed of :
            >>> 1 model world
            >>> 1 camera (PiCamera object)
            >>> 1 road follower object
    """
    __RESOLUTION = (640, 480)
    __FRAME_RATE = 32
    __VIDEO_CAPTURE_FORMAT = "bgr"

    def __init__(self, model):
        Thread.__init__(self)
        self.model = model
        self.camera = PiCamera()
        self.camera.resolution = Camera.__RESOLUTION
        self.camera.framerate = Camera.__FRAME_RATE
        self.rawCapture = PiRGBArray(self.camera, size=Camera.__RESOLUTION)
        self.roadFollower = RoadFollower()
        self.terminated = False

    def run(self):
        """
            Run function of the thread.
            The function that is launched when we start the thread.
        """

        while not self.terminated:
            self.camera.capture(self.rawCapture, format=Camera.__VIDEO_CAPTURE_FORMAT)
            frame = self.rawCapture.array
            # cv2.imshow('frame', frame)
            self.roadFollower.update_frame(frame)
            self.roadFollower.filter()
            # self.roadFollower.display_masks()

            self.model.band_ycoord = self.roadFollower.compute_strip_position()[1]
            if(self.model.band_ycoord > 0):
                self.model.sema_band_ycoord.release()

            #print(self.roadFollower.compute_strip_position())
            self.model.car.direction_motor.angle_camera = -self.roadFollower.compute_deviation()

            self.rawCapture.seek(0)
            self.rawCapture.truncate(0)

            # Sleep periode to let the hand to an other thread
            time.sleep(SLEEP_CAMERA_THREAD)

    def stop(self):
        """
            Allow to stop the thread and quit it.
        """
        self.terminated = True
        print("camera thread closed")

if __name__ == '__main__':
    cam = Camera(0)
    cam.run()
