#!/bin/bash

cd ~/LittleHelper/

while getopts ":d" opt; do
  case $opt in
    d)
      pydoc -w ./*?/[^_]*.py
      cd ./doc
      rm ./*
      find ../ -name '*.html' -exec mv -v {} . \;
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

cd ~/LittleHelper/GUI/
pyuic5 mainwindow.ui > mainwindow_temp.py
head -n -1 mainwindow_temp.py > mainwindow_auto.py
rm mainwindow_temp.py
echo "import GUI.res_rc" >> mainwindow_auto.py 
pyrcc5 res.qrc > res_rc.py
cd ..
sudo python main.py


