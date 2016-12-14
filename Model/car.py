#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The car module
    ===================

    Used to represent the car and its components

"""

import sys
import math
from . import battery, motor, sensor, path
from struct import *
from Observer import observable
import time

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

        # battery
        self.battery = battery.Battery()

        # front motor
        self.direction_motor = motor.FrontMotor()

        # rear motors
        self.rear_motors = []
        self.rear_motors.append(motor.RearMotor())
        self.rear_motors.append(motor.RearMotor())

        # sensors
        self.sensors = []
        self.sensors.append(sensor.UltrasoundSensor("avant"))
        self.sensors.append(sensor.UltrasoundSensor("avant gauche"))
        self.sensors.append(sensor.UltrasoundSensor("avant droit"))
        self.sensors.append(sensor.UltrasoundSensor("arriere"))
        self.sensors.append(sensor.UltrasoundSensor("arriere gauche"))
        self.sensors.append(sensor.UltrasoundSensor("arriere droit"))

        # distances
        self.current_distance = 0

        # ack byte
        self.init_distance_flag = False
        self.reset_distance_ack = True

        # variables usefull for the path
        self.current_path = path.Path()

    def get_ack_byte(self):
        """
        Return the ack byte according to the different information of the car

         -------------------------------------------------------------
        | 00 | 00 | 00 | 00 | 00 | 00 | reset distance | ack distance |
         -------------------------------------------------------------
        """
        # update of the reset distance bit
        bin_ack = self.dec2bin(0)
        if(self.init_distance_flag):
            bin_ack[6] = 1

        return self.bin2dec(bin_ack)


    def get_distance_ack(self):
        return self.reset_distance_ack

    def reset_distance(self):
        """
        reset_distance_flag become true when we want the distance to be reset by the STM
        """
        self.reset_distance_flag = True
        self.reset_distance_ack = False

    def update_distance(self, distance1, distance2, ack_bit):
        """
        Update the reset_distance_flag according to the ack bit
        Notify the actual path if necessary
        Update the distance

        :param distance1: The distance of the wheel 1
        :type distance1: integer
        :param distance2: The distance of the wheel 2
        :type distance2: integer
        :param ack_bit: The ack bit send by the STM
        :type distance2: binary number (0 if false, 1 if true)


        """
        # If we receive a Ack Response for reinit distance
        if(ack_bit):
            self.reset_distance_flag = False
            self.reset_distance_ack = True

        # Update the distance
        self.current_distance = (distance1 + distance2)/2

    def get_distance():
        return self.current_distance
        
    def modelToFrame(self):
        """

            The modelToFrame function
            -------------------------

            Used to translate the model into a frame that can be sent to the STM32
            Model of the frame :
                     --------------------------------------------------------
                >>> | FrontMotor | rearLeftMotor | rearRightMotor | 00....00 |
                     --------------------------------------------------------

            :return: The frame to be sent
            :rtype: String of 80 characters.

        """
        frame = ""

        # front motor
        frame = self.to_chr(self.direction_motor.getAngle())
        # rear motors
        for motor in self.rear_motors:
            frame = frame + self.to_chr(motor.getSpeed())
        # distance
        for _ in self.rear_motors:
            frame = frame + chr(0)
        # sensors
        for _ in self.sensors:
            frame = frame + chr(0)
        # battery
        frame = frame + chr(0)
        # Ack byte
        frame = frame + self.to_chr(self.get_ack_byte())

        return frame


    def frameToModel(self, dataReceived):
        """

            The frameToModel function
            -------------------------

            Used to translate a frame received from the STM to update the model
            Model of the frame v.1 :
                     -----------------------------------------------------------
                >>> | 00..00 | Distance | UltrasoundSensors | Battery | AckByte |
                     -----------------------------------------------------------

            Model for the battery:
                     ---------------------------------------
                >>> | 0..0 (7 bites) | 0/1 (charged or not) |
                     ---------------------------------------

            :param a: The received frame
            :type a: string of 80 characters

        """
        # We transform the received Frame data from hexa to integer
        recvValue = map(ord, dataReceived[1])

        # Convert a int in binary number to read each bits separately
        ack_bin = self.dec2bin(recvValue[12])

        # read distances values
        # ack for initialisation of the distance is the last bit of the byte
        self.update_distance(recvValue[3],recvValue[4], ack_bin[7] )

        # read sensors values
        i = 0
        for sensor in self.sensors:
            sensor.set_distance(recvValue[5+i])
            i+=1
        self.notify_distance_observers()

        # read battery value
        self.battery.set_charged(recvValue[11])

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
        self.current_path = path

    @staticmethod
    def to_chr(n):
        if n<0:
            res=256+n
        else:
            res=n
        return chr(res)

    @staticmethod
    def dec2bin(d,nb=8):
        """Représentation d'un nombre entier en chaine binaire (nb: nombre de bits du mot)"""
        if d == 0:
            return "0".zfill(nb)
        if d<0:
            d += 1<<nb
        b=""
        while d != 0:
            d, r = divmod(d, 2)
            b = "01"[r] + b
        return b.zfill(nb)

    @staticmethod
    def bin2dec(s):
        return int(s,2)
