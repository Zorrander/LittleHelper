#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The motor module
    ================

    Used to handle the behaviours of motors on the car.

"""

import sys
from abc import ABCMeta, abstractmethod



class Motor:
    """

        The Motor abstract class
        ------------------------

        Caracteristics :
            >>> 2 attributs
            >>> 6 abstract functions

    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.state = 0
        self.speed = 0

    @abstractmethod
    def notify():
        pass

    @abstractmethod
    def moveForward():
        pass
    @abstractmethod
    def moveBackward():
        pass
    @abstractmethod
    def stop():
        pass
    @abstractmethod
    def turnLeft():
        pass
    @abstractmethod
    def turnRight():
        pass

    def setState(state):

        """

            The setState function
            ---------------------

            Used to change the model

            Model of the state v.1 :
                     -----------------------------------------------------------
                >>> | 0=nul | 1=stop  | 2=left or forward | 3=right or backward |
                     -----------------------------------------------------------

        """
        self.state = state

    def getState():

        """

            The getState function
            ---------------------

            Used to retrieve the actual state in the model and translate it
            into the right format for the SPI communication.

        """

        tmp = ""
        tmp = tmp + '{0:b}'.format(self.state)
        while ( len(str(tmp)) < 2 ):
            tmp = '0' + tmp

        return tmp

    def setSpeed(speed):

        """

            The setState function
            ---------------------

            Used to change the model

            Model of the speed v.1 :

                >>> Only use pair values. Indicated using %.

        """

        self.speed = speed


    def getSpeed():

        """

            The getSpeed function
            ---------------------

            Used to retrieve the actual speed in the model and translate it
            into the right format for the SPI communication.

        """
        tmp = ""
        tmp = tmp + '{0:b}'.format(self.speed)
        while ( len(str(tmp)) < 6 ):
            tmp = '0' + tmp

        return tmp




class FrontMotor(Motor):

    """

        The Front motor class
        ---------------------

        Adapt the generic behaviour of Motor to control the direction of the car

    """

    def __init__(self):
        super(self.__class__, self).__init__()

    def notify():
        pass

    def moveForward(self):
        setState(1)

    def moveBackward():
        setState(1)

    def stop():
        setState(1)

    def turnLeft():
        setState(2)

    def turnRight():
        setState(3)


class RearMotor(Motor):

    """

        The Front motor class
        ---------------------

        Adapt the generic behaviour of Motor to move the car

    """

    def __init__(self):
        super(self.__class__, self).__init__()

    def moveForward(self):
        setState(2)

    def moveBackward():
        setState(3)

    def stop():
        setState(1)

    def turnLeft():
        setState(1)

    def turnRight():
        setState(1)

    def notify():
        pass


