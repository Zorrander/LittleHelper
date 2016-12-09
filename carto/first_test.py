import PIL.Image as Image
import numpy as np
import time as t
from matplotlib import pyplot as plt
from matplotlib import animation as anim

np.set_printoptions(threshold=np.nan)

class Map:
    def __init__(self,car_position):
       self.img_to_grid()
       self.init_car_position(car_position)
        
    def img_to_grid(self): 
        im = Image.open('carte_test1.bmp')
        shape = (im.height, im.width)
        data = np.array(list(im.getdata())).reshape(shape)
        self.grid = (data != 0)*1
        
    def init_car_position(self,car_position):
        self.occupancy_grid = self.grid
        self.occupancy_grid[car_position[0]][car_position[1]] = 2
        self.car_position = car_position
        
    def get_car_position(self):
        return self.car_position

    def set_car_position(self, car_position):
        if self.occupancy_grid[car_position[0]][car_position[1]] == 0:
            self.occupancy_grid[self.car_position[0]][self.car_position[1]] = 0
            self.occupancy_grid[car_position[0]][car_position[1]] = 2
            self.car_position = car_position
            return 0
        else:
            return -1
        
    def display_occup_grid(self):
        print(self.occupancy_grid)
        print('\n')
    
    def display_occup_grid_img(self):
        #self.img = Image.fromarray(self.occupancy_grid, 'L')
        #self.img.show()
        plt.imshow(self.occupancy_grid, interpolation='nearest')
        plt.show()
        
    
    def update(self,i):
        plt.imshow(self.occupancy_grid, interpolation='nearest')
        self.set_car_position([7,i])
        
    
map_car = Map([6,0])
fig = plt.figure()
a = anim.FuncAnimation(fig, map_car.update, frames=50, repeat=False, interval = 1000)
plt.show()