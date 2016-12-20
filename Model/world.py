

from car import Car
from path import Path
class World():

    def __init__(self, car):
        self.car = car
        self.path = Path()
        self.current_distance = 0
        self.reset_distance = False

    @property
    def car(self):
        return self.car

    @property
    def path(self):
        return self.path

    @property
    def current_distance(self):
        return self.current_distance

    @property
    def reset_distance_flag(self):
        return self.reset_distance_flag

    @property
    def reset_distance_ack(self):
        return self.reset_distance_ack

    def set_distance(self, distance1, distance2):
        self.current_distance = (distance1 + distance2)/2
