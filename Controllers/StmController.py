#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    The Stm module
    ==============

    Used to handle the communication between the RaspberryPi and the STM32.

"""

import wiringpi
import time
from threading import Thread
from constant import SLEEP_STMCONTROLLER_THREAD

class StmController(Thread):

    """

        The Stm Class
        -------------

        Start a new thread commuincating with the STM32 and define its behaviour.

    """

    def __init__(self, model):
        self.model = model
        self.car = model.car
        self.SPIchannel = 0
        SPIspeed = 562500
        wiringpi.wiringPiSetupGpio()
        wiringpi.wiringPiSPISetupMode(self.SPIchannel, SPIspeed, 0)
        self.terminated = False
        Thread.__init__(self)

    def run(self):
        while not self.terminated:
            sendData = self.modelToFrame()
            recvData = wiringpi.wiringPiSPIDataRW(self.SPIchannel, sendData)
            self.frameToModel(recvData)

            # Sleep periode to let the hand to an other thread
            time.sleep(SLEEP_STMCONTROLLER_THREAD)

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
            :rtype: String

        """
        frame = ""

        # front motor
        frame = self.to_chr(self.model.car.direction_motor.angle)
        # rear motors
        for motor in self.model.car.rear_motors:
            frame = frame + self.to_chr(motor.speed)
        # distance
        for _ in self.model.car.rear_motors:
            frame = frame + chr(0)
        # sensors
        for _ in self.model.car.sensors:
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


        self.set_ack_byte(recvValue[12])

        # read distances values
        # ack for initialisation of the distance is the last bit of the byte
        self.model.current_distance = (recvValue[3] + recvValue[4])/2

        # read sensors values
        i = 0
        for sensor in self.model.car.sensors:
            sensor.distance = recvValue[5+i]
            i+=1
#        self.notify_distance_observers()

        # read battery value
        self.model.car.battery.charged = recvValue[11]

    @staticmethod
    def to_chr(n):
        if n<0:
            res=256+n
        else:
            res=n
        return chr(res)

    def get_ack_byte(self):
        """
        Return the ack byte according to the different information of the car

         -------------------------------------------------------------
        | 00 | 00 | 00 | 00 | 00 | 00 | reset distance | ack distance |
         -------------------------------------------------------------
        """
        # update of the reset distance bit
        bin_ack = self.dec2bin(0)
        if(self.model.reset_distance):
            tmp = list(bin_ack)
            tmp[6] = '1'
            bin_ack = "".join(tmp)

        return self.bin2dec(bin_ack)

    def set_ack_byte(self, ack_byte):
        """
        Update the different information of the car according to the ack byte

         -------------------------------------------------------------
        | 00 | 00 | 00 | 00 | 00 | 00 | reset distance | ack distance |
         -------------------------------------------------------------
        """
        # Convert a int in binary number to read each bits separately
        ack_bin = self.dec2bin(ack_byte)
        # update of the ack reset distance bit
        self.model.ack_reset_distance = int(ack_bin[7])
        if(self.model.ack_reset_distance):
            self.model.reset_distance = False

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

    def stop(self):
        self.terminated = True
