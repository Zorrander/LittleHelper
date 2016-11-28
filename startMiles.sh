#!/bin/bash

cd /home/angleraud/LittleHelper/GUI/
pyuic5 mainwindow.ui > mainwindow_temp.py
head -n -1 mainwindow_temp.py > mainwindow_auto.py
rm mainwindow_temp.py
echo "import GUI.res_rc" >> mainwindow_auto.py 
pyrcc5 res.qrc > res_rc.py
cd ..
python3 main.py
