#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The Stm module
    ==============

    Used to handle the communication between the RaspberryPi and the STM32.

"""

import sys
from Model import car
#import wiringpi
import time
from threading import Thread


class StmController(Thread):

    """

        The Stm Class
        -------------

        Start a new thread commuincating with the STM32 and define its behaviour.

    """

    def __init__(self, model):
        self.model = model
        self.lengthFrame = 10
        self.SPIchannel = 0
        self.SPIspeed = 500000
        #wiringpi.wiringPiSetupGpio()
        #wiringpi.wiringPiSPISetup(SPIchannel, SPIspeed)
        Thread.__init__(self)

    def run(self):

        while(1):
            sendData = buildFrame()
            #recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
            recvData("only for test")
            updateModel(recvData)


    def buildFrame(self):

        """
            The buildFrame function
            -----------------------

            Used to ask the model for its actual state
        """
        self.model.modelToFrame(self.lengthFrame)

    def updateModel(self, data):

        """
            The updateModel function
            ------------------------

            Used to update the model with the new informations from the STM32.
        """
        self.model.frameToModel(data)
