"""
    The check distance module
    =========================
    Used to reset the distance with band on the road checking 
"""

from multiprocessing import Process
from constant import FRAME_EDGE, BAND_THRESHOLD

class checkDistance(Process):
    
    def __init__(self, band_xcoord, sema_band_xcoord, distance, sema_distance): 
        
        """
            band_xcoord : shared value with video process
            distance : shared value with spi process
            sema_band_xcoord : semaphore[1] shared with video process
            sema_distance : semaphore[1] shared with spi process
        """
        
        Process.__init__(self)
        self.band_xcoord = band_xcoord
        self.sema_band_xcoord = sema_band_xcoord
        self.distance = distance
        self.sema_distance = sema_distance
        self.band_list = [500, 1000, 1500, 2000, 2500]
        
    def run(self):
        
        while(1):
            self.sema_band_xcoord.acquire() #wait from the video process to release the semaphore when a band is seen
            if(FRAME_EDGE - self.band_xcoord < BAND_THRESHOLD):
                #use another function that min for later, to accelerate processing. Check the list with a cursor. Assuming that the right band cannot be backward but is always forward.
                #if cursor is on item 2, compare the distance with band item 2 and 3. If closest from item 2, take this one. If closest from item 3, compare also with item 4 and so on.
                self.distance = min(self.band_list, key=lambda x:abs(x-self.distance))  #find the closest band from the distance received from odometry 
                self.sema_distance.release() #release the semaphore to signal to spi process that the distance is reset to the right value
                