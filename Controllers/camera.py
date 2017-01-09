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
        time.sleep(0.1)

    def run(self):
        for stream in self.camera.capture_continuous(self.rawCapture, format=Camera.__VIDEO_CAPTURE_FORMAT, use_video_port=True):
            frame = stream.array
            cv2.imshow('frame', frame)
            self.roadFollower.update_frame(frame)
            self.roadFollower.filter()
            # self.model.car.direction_motor.angle = self.roadFollower.compute_deviation()
            self.rawCapture.truncate(0)

            # if the `q` key was pressed, break from the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        time.sleep(SLEEP_CAMERA_THREAD)


if __name__ == '__main__':
    cam = Camera(0)
    cam.start() 
