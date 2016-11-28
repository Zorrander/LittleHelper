#-------------------------------------------------
#
# Project created by QtCreator 2016-11-17T16:10:33
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = GUI
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui

RESOURCES += \
    res.qrc

DISTFILES += \
    Tabs/command.py \
    Tabs/index.py \
    Tabs/motors.py \
    Tabs/myPaths.py \
    Tabs/overview.py \
    ../main.py \
    Tabs/window.py \
    ../Model/battery.py \
    ../Model/car.py \
    ../Model/motor.py \
    ../Model/sensor.py \
    ../Controllers/window.py \
    ../Observer/observable.py \
    ../Observer/observer.py \
    ../Controllers/StmController.py
