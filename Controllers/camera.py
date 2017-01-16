# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from road_follower import RoadFollower
from threading import Thread
from constant import *
import time
import cv2

class Camera(Thread):

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
        time.sleep(0.1)

    def run(self):
        while not self.terminated:
            self.camera.capture(self.rawCapture, format=Camera.__VIDEO_CAPTURE_FORMAT)
            frame = self.rawCapture.array
#            cv2.imshow('frame', frame)
            self.roadFollower.update_frame(frame)
            self.roadFollower.filter()
            self.model.car.direction_motor.angle = self.roadFollower.compute_deviation()
            
            self.rawCapture.seek(0)
            self.rawCapture.truncate(0)

            time.sleep(SLEEP_CAMERA_THREAD)

    def stop(self):
        self.terminated = True

if __name__ == '__main__':
    cam = Camera(0)
    cam.start() 
