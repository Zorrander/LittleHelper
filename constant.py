import numpy as np

FORWARD = 0
BACKWARD = 1
STOP = 2
# direction
LEFT = 0
RIGHT = 1

#camera
FRAME_EDGE = 480
BAND_THRESHOLD = 20


# Sleep for the thread
SLEEP_PRELOADEDPATH_THREAD = 0.01
SLEEP_STMCONTROLLER_THREAD = 0.01
SLEEP_CHECKDISTANCE_THREAD = 0
SLEEP_CAMERA_THREAD = 0.01

# Semaphore

BLOCKING = True
NON_BLOCKING = False

# color thresholds
LOWER_GRAY = np.array([0, 0, 20])
UPPER_GRAY = np.array([200, 40, 200])

LOWER_BLUE = np.array([100, 30, 0])
UPPER_BLUE = np.array([140, 200, 230])
