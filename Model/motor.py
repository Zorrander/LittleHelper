#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The motor module
    ================

    Used to handle the behaviours of motors on the car.

"""

class FrontMotor():
    """
        Used to represent the front motor to control the direction of the car

        Caracteristics :
           >>> an angle to turn
    """

    def __init__(self):
        self.angle = 0

    def turnLeft(self, angle):
        """
            Used to set the angle for turning to the left.

            :param angle: The angle to turn (0..45)
            :type ange: int
        """
        self.angle = angle

    def turnRight(self, angle):
        """
            Used to set the angle for turning to the right.

            :param angle: The angle to turn (0..45)
            :type ange: int
        """
        self.angle = -angle

    def turn(self, angle):
        """
            Used to set the angle for turning.

            :param angle: The angle to turn (-45..45)
            :type ange: int
        """
        self.angle = angle

    @property
    def angle(self):
        """
            The angle to turn

            :getter: Returns the angle
            :setter: Sets the angle
            :type: int
        """
        return self.angle

class RearMotor():
    """
        Used to represent the rear motor to control the speed of the car

        Caracteristics :
           >>> a speed
    """

    def __init__(self):
        self.speed = 0

    def moveForward(self, speed):
        """
            Used to set the speed for moving forward.

            :param speed: The speed of the car
            :type speed: int
        """
        self.speed = speed

    def moveBackward(self, speed):
        """
            Used to set the speedfor moving backward.

            :param speed: The speed of the car
            :type speed: int
        """
        self.speed = -speed

    def stop(self):
        """
            Used to stop the car ie set the speed to 0
        """
        self.speed = 0

    @property
    def speed(self):
        """
            The speed of the car

            :getter: Returns the speed
            :setter: Sets the speed
            :type: int
        """
        return self.speed
