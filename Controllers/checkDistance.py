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

    def __init__(self, model, band_xcoord):

        """
            model : The world, model of the car and their environment
            band_xcoord : shared value with video process
            sema_band_xcoord : semaphore[1] shared with video process
        """

        Thread.__init__(self)
        self.model = model
        self.band_xcoord = band_xcoord
        self.band_list = [500, 1000, 1500, 2000, 2500]

    def run(self):

        while(1):
            self.model.sema_band_xcoord.acquire(BLOCKING) #wait from the video process to release the semaphore when a band is seen
            if(FRAME_EDGE - self.band_xcoord < BAND_THRESHOLD):
                #use another function that min for later, to accelerate processing. Check the list with a cursor. Assuming that the right band cannot be backward but is always forward.
                #if cursor is on item 2, compare the distance with band item 2 and 3. If closest from item 2, take this one. If closest from item 3, compare also with item 4 and so on.
                self.model.real_distance = min(self.band_list, key=lambda x:abs(x-self.distance))  #find the closest band from the distance received from odometry
                self.model.sema_distance.release() #release the semaphore to signal to spi process that the distance is reset to the right value

            # Sleep periode to let the hand to an other thread
            time.sleep(SLEEP_CHECKDISTANCE_THREAD)
