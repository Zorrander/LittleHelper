import PIL.Image as Image 
import numpy as np 
import time 
import sys 
import random

import os 
#QT_API = QT_API_PYQT5
print os.environ.get('QT_API')

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QTabWidget, QWidget
from PyQt5.QtCore import pyqtSignal

import matplotlib 
matplotlib.use("Qt5Agg", force=True)
#matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
print("\n\n\n ok \n\n\n")
#plt.plot(range(10))
#plt.show()
print("\n\n\n ok \n\n\n")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


from threading import Thread
from Model import car 

np.set_printoptions(threshold=np.nan) #pretty array printing

class Display:
    def __init__(self, map_car, model):
        self.a = QApplication(sys.argv)
        self.map_car = map_car
        self.model = model
        self.w = QMainWindow()
        self.sig = pyqtSignal()
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
            self.map_car.set_car_position(self.model.get_position())
#            self.sig.emit(pyqtSignal("updatePlot()"))
            self.sig.emit()
            time.sleep(2)
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
        with Image.open('carto/carte_test1.bmp') as im:
            width, height = im.size 
#        im = Image.open('carto/carte_test1.bmp')
            shape = (height, width)
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
        
    
#map_car = Map([6,0])
#display_car = Display(map_car)
#display_car.a.connect(display_car.a, SIGNAL('updatePlot()'), display_car.updateFunction)

#t = Thread(target=display_car.triggerUpdate);
#t.start();
#display_car.w.showMaximized()

#sys.exit(display_car.a.exec_())
