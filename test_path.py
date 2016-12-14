from Model import car
from Controllers import preloadedPath, StmController
#from Map import map

#from PyQt5.QtCore import pyqtSignal
import time

def test():
    model = car.Car()
    pPath = preloadedPath.PreloadedPaths(model)
    spi = StmController.StmController(model)
    spi.start()
#    pPath.start()

#    map_car = map.Map([100,100])
#    display_car = map.Display(map_car, model)
#    display_car.sig.connect(display_car.a, display_car.updateFunction)
#    display_car.sig.connect(display_car.updateFunction)
#    t = Thread(target=display_car.triggerUpdate);
#    t.start();
#    display_car.w.showMaximized()
#    sys.exit(display_car.a.exec_())
    print("lancement du path 1")
    pPath.start_path(0)

def test2():
    print("turn right 40")
    model.turnRight(40)
    time.sleep(2)

    print("turn left 40")
    model.turnLeft(40)
    time.sleep(2)

    print("turn left 0")
    model.turnLeft(0)
    time.sleep(2)

    print("turn right 40")
    model.turnRight(40)
    time.sleep(2)

    print("turn left 40")
    model.turnLeft(40)
    time.sleep(2)

    print("turn right 0")
    model.turnRight(0)
    time.sleep(2)

    print("turn right 40")
    model.turnRight(40)
    time.sleep(2)

    print("turn right 0")
    model.turnRight(0)
    time.sleep(2)

    print("turn left 0")
    model.turnLeft(0)

test()
