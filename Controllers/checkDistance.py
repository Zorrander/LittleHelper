"""
    The check distance module
    =========================
    Used to reset the distance with band on the road checking
"""

import time
from bisect import bisect_left
from threading import Thread
from constant import FRAME_EDGE, BAND_THRESHOLD, SLEEP_CHECKDISTANCE_THREAD, \
    BLOCKING


class CheckDistance(Thread):
    """
        The CheckDistance is composed of :
            >>> 1 model : The world, model of the car and their environment
            >>> 1 band_xcoord : shared value with video process
    """

    def __init__(self, model):
        Thread.__init__(self)
        self.model = model
        self.band_list = [500, 1000]
        self.cursor = 0
        self.terminated = False

    def run(self):
        """
            Run function of the thread.
            The function that is launch when we start the thread.
        """
        while(1):
            # Wait from the video process to release the semaphore when a band is seen
            self.model.sema_band_ycoord.acquire(BLOCKING)
           
            if(self.model.band_ycoord > BAND_THRESHOLD):
                #Find the closest band from the distance received from odometry
                # Different methods
               
                #Method 1
                self.model.real_distance = self.findClosest(self.band_list, self.model.current_distance)
				# TODO 
				# SI current distance et real distance != +-20% => on prend pas en compte la bande
				# donc pas de release
				
				
                print("recalibrate: ", self.model.real_distance)               
                # Method 2
                #self.model.real_distance = min(self.band_list, key=lambda(band):abs(band-self.model.current_distance))
                
                #Method 3
                # Check the list with a cursor.
                # If cursor is on item 2, compare the distance with band item 2 and 3.
                # If closest from item 2, take this one. If closest from item 3, compare also with item 4 and so on.
                
                # Release the semaphore to signal to spi process that the distance is reset to the right value
                self.model.sema_distance.release()

            # Sleep periode to let the hand to an other thread
            time.sleep(SLEEP_CHECKDISTANCE_THREAD)

    def stop(self):
        """
            Allow to stop the thread and quit it.
        """
        self.terminated = True
        
        
    @staticmethod
    def findClosest(list, number):
        #The list has to be sorted
        
        pos = bisect_left(list, number)
        if pos == 0:
            return list[0]
        if pos == len(list):
            return list(-1)
        before = list[pos-1]
        after = list[pos]
        if(after - number < number - before):
            return after
        else:
            return before
    
