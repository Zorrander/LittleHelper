import numpy as np

# Action of the car
FORWARD = 0
BACKWARD = 1
STOP = 2
TURN_LEFT = 0
TURN_RIGHT = 1

#camera
FRAME_EDGE = 480
BAND_THRESHOLD = 20


# Sleep for the thread
SLEEP_PRELOADEDPATH_THREAD = 0.01
SLEEP_STMCONTROLLER_THREAD = 0
SLEEP_CHECKDISTANCE_THREAD = 0

# Semaphore

BLOCKING = True
NON_BLOCKING = False

# color thresholds
LOWER_GRAY = np.array([0, 0, 20])
UPPER_GRAY = np.array([200, 40, 200])

LOWER_BLUE = np.array([100, 30, 0])
UPPER_BLUE = np.array([140, 200, 230])
