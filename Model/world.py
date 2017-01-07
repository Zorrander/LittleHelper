

from car import Car
from path import Path
class World(object):

    def __init__(self, car):
        self.__car = car
        self.__path = Path()
        self.__current_distance = 0
        self.__reset_distance = False

    @property
    def car(self):
        return self.__car
    @car.setter
    def car(self, value):
        self.__car = value

    @property
    def path(self):
        return self.__path
    @path.setter
    def path(self, value):
        self.__path = value

    @property
    def current_distance(self):
        return self.__current_distance
    @current_distance.setter
    def current_distance(self, value):
        self.__current_distance = value

    @property
    def reset_distance(self):
        return self.__reset_distance
    @reset_distance.setter
    def reset_distance(self, value):
        self.__reset_distance = value

    def set_distance(self, distance1, distance2):
        self.current_distance = (distance1 + distance2)/2
