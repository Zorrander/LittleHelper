#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The car module
    ===================

    Used to represent the car and its components

"""

import sys
from . import battery, motor, sensor
from struct import *
from Observer import observable

class Car(observable.Observable):

    def __init__(self):

        """

            The init function
            -----------------

            Little Helper v.1 :
                >>> 1 battery
                >>> 1 front motor to control the direction
                >>> 2 rear motors to move the car
                >>> 6 ultrasound sensors to detect obstacles

        """
        observable.Observable.__init__(self)
        self.battery = battery.Battery()
        self.motors = []
        self.motors.append(motor.FrontMotor())
        self.motors.append(motor.RearMotor())
        self.motors.append(motor.RearMotor())
        self.sensors = []
        self.sensors.append(sensor.UltrasoundSensor())
        self.sensors.append(sensor.UltrasoundSensor())
        self.sensors.append(sensor.UltrasoundSensor())
        self.sensors.append(sensor.UltrasoundSensor())
        self.sensors.append(sensor.UltrasoundSensor())
        self.sensors.append(sensor.UltrasoundSensor())

    def modelToFrame(lengthFrame):
        """

            The modelToFrame function
            -------------------------

            Used to translate the model into a frame that can be sent to the STM32
            Model of the frame v.1 :
                     --------------------------------------------------------
                >>> | FrontMotor | rearLeftMotor | rearRightMotor | 00....00 |
                     --------------------------------------------------------

            Model for one motor :
                     -----------------------------------
                >>> | State (2 bites) | speed (6 bites) |
                     -----------------------------------

            :param a: The length of the frame to be sent
            :type a: int
            :return: The frame to be sent
            :rtype: String of 80 characters.

        """
        frame = ""

        for motor in self.motors:
            frame = frame + motor.getState() + motor.getSpeed()

        for sensor in self.sensors:
            frame = frame + sensor.fillFrame()

        frame = frame + battery.fillFrame()
        
        return frame


    def frameToModel(dataReceived):
        """

            The frameToModel function
            -------------------------

            Used to translate a frame received from the STM to update the model
            Model of the frame v.1 :
                     --------------------------------------
                >>> | 00..00 | UltrasoundSensors | Battery |
                     --------------------------------------

            Model for one sensor:
                     ---------------------------------------
                >>> | 0..0 (7 bites) | 0/1 (charged or not) |
                     ---------------------------------------

            For the battery:
                >>>

            :param a: The received frame
            :type a: string of 80 characters

        """
        notify_observers(self, dataReceived)



    def moveForward():
        """

            The moveForward function
            -------------------------

            Used to transmite the command to move forward to all the motors.

        """
        for motor in self.motors:
            motor.moveForward

    def moveBackward():
        """

            The moveForward function
            -------------------------

            Used to transmite the command to move backward to all the motors.

        """
        for motor in self.motors:
            motor.moveBackward

    def stop():
        """

            The moveForward function
            -------------------------

            Used to transmite the command to stop to all the motors.

        """
        for motor in self.motors:
            motor.stop

    def turnLeft():
        """

            The moveForward function
            -------------------------

            Used to transmite the command to turn left to all the motors.

        """
        for motor in self.motors:
            motor.turnLeft

    def turnRight():
        """

            The moveForward function
            -------------------------

            Used to transmite the command to turn right to all the motors.

        """
        for motor in self.motors:
            motor.turnRight







