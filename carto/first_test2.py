import PIL.Image as Image
import numpy as np
import time
from matplotlib import pyplot as plt
from matplotlib import animation as anim
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
import sys
from PyQt4.QtGui import QApplication, QMainWindow, QVBoxLayout,QTabWidget, QWidget
from PyQt4.QtCore import SIGNAL
from threading import Thread
import random

np.set_printoptions(threshold=np.nan) #pretty array printing

class Display:
    def __init__(self, map_car):
        self.a = QApplication(sys.argv)
        self.map_car = map_car
        self.w = QMainWindow()
        t = QTabWidget(self.w)
        Tab1 = QWidget()
        t.addTab(Tab1, '1st Plot')
        t.resize(1280, 300)
        
        self.fig, ax = plt.subplots()
        ax.set(title='Car progressing')
        self.im = ax.imshow(map_car.get_occupancy_grid(), interpolation='nearest')
        
        layout = QVBoxLayout();
        layout.addWidget(FigureCanvasQTAgg(self.fig));
        Tab1.setLayout(layout);
        
    def triggerUpdate(self):
        while True:
            self.map_car.set_car_position([7,random.randint(0,99)])
            self.a.emit(SIGNAL('updatePlot()'));
            time.sleep(2);
            print('update triggered!\n')
            
    def updateFunction(self):
        self.im.set_data(self.map_car.get_occupancy_grid())
        self.fig.canvas.draw()
        print('update done!\n')

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
        
    def get_occupancy_grid(self):
        return self.occupancy_grid
        
    
    def update_plot(self,i):
        plt.imshow(self.occupancy_grid, interpolation='nearest')
        self.set_car_position([7,i])
        
    
map_car = Map([6,0])
display_car = Display(map_car)
display_car.a.connect(display_car.a, SIGNAL('updatePlot()'), display_car.updateFunction)

t = Thread(target=display_car.triggerUpdate);
t.start();
display_car.w.showMaximized()

sys.exit(display_car.a.exec_())