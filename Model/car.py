#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The car module
    ===================

    Used to represent the car and its components

"""

from battery import Battery
from motor import FrontMotor, RearMotor
from sensor import UltrasoundSensor

class Car():

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

        # battery
        self.battery = Battery()

        # front motor
        self.direction_motor = FrontMotor()

        # rear motors
        self.rear_motors = []
        self.rear_motors.append(RearMotor())
        self.rear_motors.append(RearMotor())

        # sensors
        self.sensors = []
        self.sensors.append(UltrasoundSensor("front"))
        self.sensors.append(UltrasoundSensor("front left"))
        self.sensors.append(UltrasoundSensor("front right"))
        self.sensors.append(UltrasoundSensor("rear"))
        self.sensors.append(UltrasoundSensor("rear left"))
        self.sensors.append(UltrasoundSensor("rear right"))

    @property
    def battery(self):
        return self.battery

    @property
    def direction_motor(self):
        return self.direction_motor

    @property
    def rear_motors(self):
        return self.rear_motors

    @property
    def sensors(self):
        return self.sensors

    @property
    def rear_motors(self):
        return self.rear_motors

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

            Used to transmite the command to turn left to the direction motor.

        """
        self.direction_motor.turnLeft(angle)

    def turnRight(self,angle):
        """

            The turnRight function
            -------------------------

            Used to transmite the command to turn right to the direction motor.

        """
        self.direction_motor.turnRight(angle)
