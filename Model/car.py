#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The car module
    ==============

    Used to represent the car and its components

"""

from battery import Battery
from motor import FrontMotor, RearMotor
from sensor import UltrasoundSensor

class Car():
    """
        Little Helper v.1 :
            >>> 1 battery
            >>> 1 front motor to control the direction
            >>> 2 rear motors to move the car
            >>> 6 ultrasound sensors to detect obstacles
    """

    def __init__(self):
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
        """
            The battery of the car

            :getter: Returns the battery object
            :setter: Sets the battery object
            :type: Battery
        """
        return self.battery

    @property
    def direction_motor(self):
        """
            The direction motor of the car

            :getter: Returns the direction_motor object
            :setter: Sets the direction_motor object
            :type: FrontMotor
        """
        return self.direction_motor

    @property
    def rear_motors(self):
        """
            The list of the rear motor of the car

            :getter: Returns the list of rear_motor object
            :setter: Sets the list of rear_motor object
            :type: RearMotor[]
        """
        return self.rear_motors

    @property
    def sensors(self):
        """
            The list of the sensors of the car

            :getter: Returns the list of sensors object
            :setter: Sets the list of sensors object
            :type: UltrasoundSensor[]
        """
        return self.sensors

    def moveForward(self, speed):
        """
            Used to transmite the command to move forward to all the motors.

            :param speed: The speed of the car
            :type speed: int

        """
        for motor in self.rear_motors:
            motor.moveForward(speed)

    def moveBackward(self, speed):
        """
            Used to transmite the command to move backward to all the motors.

            :param speed: The speed of the car
            :type speed: int

        """
        for motor in self.rear_motors:
            motor.moveBackward(speed)

    def stop(self):
        """
            Used to transmite the command to stop to all the motors.
        """
        for motor in self.rear_motors:
            motor.stop()

    def turnLeft(self, angle):
        """
            Used to transmite the command to turn left to the direction motor.

            :param angle: The angle to turn (0..45)
            :type ange: int

        """
        self.direction_motor.turnLeft(angle)

    def turnRight(self,angle):
        """
            Used to transmite the command to turn right to the direction motor.

            :param angle: The angle to turn (0..45)
            :type ange: int

        """
        self.direction_motor.turnRight(angle)

    def turn(self,angle):
        """
            Used to transmite the command to turn to the direction motor.

            :param angle: The angle to turn (-45..45)
            :type ange: int

        """
        self.direction_motor.turn(angle)
