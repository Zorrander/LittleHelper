"""
    The check distance module
    =========================
    Used to reset the distance with band on the road checking
"""

import time
from threading import Thread
#from constant import SLEEP_DETECTOBSTACLE_THREAD 

class DetectObstacle(Thread):

    def __init__(self, model):
        Thread.__init__(self)
        self.model = model
        self.terminated = False

    def run(self):
        """
            Run function of the thread.
            The function that is launch when we start the thread.
        """
        while not self.terminated:
            print(self.model.car.sensors[0].distance)
            if(self.model.car.sensors[0].distance < 50): #sensor avant gauche
            #and self.model.car.sensors[1].distance < 70 and self.model.car.sensors[2].distance < 70):
                self.model.sema_obstacle.release()
                
               
            time.sleep(0.01)

    def stop(self):
        """
            Allow to stop the thread and quit it.
        """
        self.terminated = True
        print("detect_obstacle thread closed")
