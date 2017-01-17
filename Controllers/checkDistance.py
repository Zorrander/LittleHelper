"""
    The check distance module
    =========================
    Used to reset the distance with band on the road checking
"""

import time

from threading import Thread
from constant import FRAME_EDGE, BAND_THRESHOLD, SLEEP_CHECKDISTANCE_THREAD, \
    BLOCKING


class CheckDistance(Thread):
    """
        The CheckDistance is composed of :
            >>> 1 model : The world, model of the car and their environment
            >>> 1 band_xcoord : shared value with video process
    """

    def __init__(self, model, band_xcoord):
        Thread.__init__(self)
        self.model = model
        self.band_xcoord = band_xcoord
        self.band_list = [500, 1000, 1500, 2000, 2500]
        self.terminated = False

    def run(self):
        """
            Run function of the thread.
            The function that is launch when we start the thread.
        """
        while(1):
            # Wait from the video process to release the semaphore when a band is seen
            self.model.sema_band_xcoord.acquire(BLOCKING)
            if(FRAME_EDGE - self.band_xcoord < BAND_THRESHOLD):
                # Use another function that min for later, to accelerate processing.
                # Check the list with a cursor. Assuming that the right band cannot be backward but is always forward.
                # If cursor is on item 2, compare the distance with band item 2 and 3.
                # If closest from item 2, take this one. If closest from item 3, compare also with item 4 and so on.

                # Find the closest band from the distance received from odometry
                self.model.real_distance = min(self.band_list, key=lambda x:abs(x-self.distance))
                # Release the semaphore to signal to spi process that the distance is reset to the right value
                self.model.sema_distance.release()

            # Sleep periode to let the hand to an other thread
            time.sleep(SLEEP_CHECKDISTANCE_THREAD)

    def stop(self):
        """
            Allow to stop the thread and quit it.
        """
        self.terminated = True
