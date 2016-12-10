#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The car module
    ===================

    Used to represent the car and its components

"""

import sys
from . import battery, motor, sensor, path
from struct import *
from Observer import observable

FRONT_SENSOR = 0
FRONT_LEFT_SENSOR = 1
FRONT_RIGHT_SENSOR = 2
REAR_SENSOR = 3
REAR_LEFT_SENSOR = 4
REAR_RIGHT_SENSOR = 5

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
	
        self.direction_motor = motor.FrontMotor()

        self.rear_motors = [] 
        self.rear_motors.append(motor.RearMotor())
        self.rear_motors.append(motor.RearMotor())
        self.sensors = []
        self.sensors.append(sensor.UltrasoundSensor(FRONT_SENSOR))
        self.sensors.append(sensor.UltrasoundSensor(FRONT_LEFT_SENSOR))
        self.sensors.append(sensor.UltrasoundSensor(FRONT_RIGHT_SENSOR))
        self.sensors.append(sensor.UltrasoundSensor(REAR_SENSOR))
        self.sensors.append(sensor.UltrasoundSensor(REAR_LEFT_SENSOR))
        self.sensors.append(sensor.UltrasoundSensor(REAR_RIGHT_SENSOR))

        self.actual_path = path.Path()

    def modelToFrame(self):
        """

            The modelToFrame function
            -------------------------

            Used to translate the model into a frame that can be sent to the STM32
            Model of the frame v.1 :
                     --------------------------------------------------------
                >>> | FrontMotor | rearLeftMotor | rearRightMotor | 00....00 |
                     --------------------------------------------------------

            Model for front motor : 
                     -----------------------------------
                >>> | State (2 bites) | angle (6 bites) |
                     -----------------------------------

            Model for rear motor :
                     -----------------------------------
                >>> | State (2 bites) | speed (6 bites) |
                     -----------------------------------

            :param a: The length of the frame to be sent
            :type a: int
            :return: The frame to be sent
            :rtype: String of 80 characters.

        """
        frame = ""
	
        frame = self.to_chr(self.direction_motor.getAngle())
	
        for motor in self.rear_motors:
            frame = frame + self.to_chr(motor.getSpeed())
        
        for _ in self.rear_motors:
            frame = frame + chr(0) # distance 
        for _ in self.sensors:
            frame = frame + chr(0) # sensor

        frame = frame + chr(0) # battery

        return frame


    def frameToModel(self, dataReceived):
        """

            The frameToModel function
            -------------------------

            Used to translate a frame received from the STM to update the model
            Model of the frame v.1 :
                     -------------------------------------------------
                >>> | 00..00 | Distance | UltrasoundSensors | Battery |
                     -------------------------------------------------

            Model for the battery:
                     ---------------------------------------
                >>> | 0..0 (7 bites) | 0/1 (charged or not) |
                     ---------------------------------------

            :param a: The received frame
            :type a: string of 80 characters

        """
        # We transform the received Frame data from hexa to integer
        recvValue = map(ord, dataReceived[1])
        self.actual_path.set_distance(recvValue[3],recvValue[4])
        i = 0  
        for sensor in self.sensors :
            sensor.set_distance(recvValue[5+i])
            i = i+1
        self.notify_distance_observers()      
#        self.battery.set_charged(recvValue[11])



    def moveForward(self, speed):
        """

            The moveForward function
            -------------------------

            Used to transmite the command to move forward to all the motors.

        """
        for motor in self.rear_motors:
            motor.moveForward(speed)

    def moveBackward(self, speed):
        """

            The moveForward function
            -------------------------

            Used to transmite the command to move backward to all the motors.

        """
        for motor in self.rear_motors:
            motor.moveBackward(speed)

    def stop(self):
        """

            The moveForward function
            -------------------------

            Used to transmite the command to stop to all the motors.

        """
        for motor in self.rear_motors:
            motor.stop()

    def turnLeft(self, angle):
        """

            The turnLeft function
            -------------------------

            Used to transmite the command to turn left to all the motors.

        """
        self.direction_motor.turnLeft(angle)

    def turnRight(self,angle):
        """

            The turnRight function
            -------------------------

            Used to transmite the command to turn right to all the motors.

        """
        self.direction_motor.turnRight(angle)


    def set_path(self, path):
        self.actual_path = path

    @staticmethod
    def to_chr(n):
        if n<0:
            res=256+n
        else:
            res=n
        return chr(res)

