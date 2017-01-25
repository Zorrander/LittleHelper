# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import math
from road_follower import *

def onMouse(event, x, y, flag, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(param[y][x])

road_follow = RoadFollower()
simulation = np.zeros((200,400,3),np.uint8)

# init camera
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))

# allow camera to warmup
time.sleep(0.1)

cv2.namedWindow("hsv")

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array

	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	cv2.setMouseCallback('hsv', onMouse, param=hsv)
	# cv2.imshow("Frame", image)
	if image is None:
		break
	road_follow.update_frame(image)
	road_follow.filter()
	road_follow.display_masks()
	alpha = road_follow.compute_deviation()
	coor = road_follow.compute_strip_position()
	print(coor)
	cv2.circle(hsv, (coor[0], coor[1]), 5, (255, 255, 255), thickness=5)
	cv2.imshow("hsv", hsv)

	if alpha >= 45.0:
		alpha = 45.0
	elif alpha <= -45.0:
		alpha = -45.0
	point_a = (200, 150)
	point_b = (int(200 + 100 * math.tan(math.radians(alpha))), 50)
	cv2.line(simulation, point_a, point_b, (255, 0, 0), thickness=5)
	cv2.imshow("sim", simulation)
	simulation = np.zeros((200, 400, 3), np.uint8)
	


	key = cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)
	if key == ord("q"):
		break
