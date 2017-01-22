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
        Start a new thread commuincating with the STM32 and define its behaviour.

        The stmController is composed of :
            >>> 1 model world
            >>> spi communication information
    """

    def __init__(self, model):
        # The world model
        self.model = model

        # Initialisation of the SPI communication
        self.SPIchannel = 0
        SPIspeed = 562500
        wiringpi.wiringPiSetupGpio()
        wiringpi.wiringPiSPISetupMode(self.SPIchannel, SPIspeed, 0)

        # Boolean that allow the thread to be quit
        self.terminated = False

        # Initialise the thread
        Thread.__init__(self)

    def run(self):
        """
            Run function of the thread.
            The function that is launch when we start the thread.
        """
        # Infinit loop util the programm quit
        while not self.terminated:
            sendData = self.modelToFrame()
            recvData = wiringpi.wiringPiSPIDataRW(self.SPIchannel, sendData)
            self.frameToModel(recvData)

            # Sleep periode to let the hand to another thread
            time.sleep(SLEEP_STMCONTROLLER_THREAD)

    def modelToFrame(self):
        """
            Used to translate the model into a frame that can be sent to the STM32

            Model of the frame :
                >>>  --------------------------------------------------------
                >>> | FrontMotor | rearLeftMotor | rearRightMotor | 00....00 |
                >>>  --------------------------------------------------------

            :return: The frame to be sent
            :rtype: str
        """
        frame = ""

        # front motor
        frame = self.to_chr(self.model.car.direction_motor.angle)
        # rear motors
        for motor in self.model.car.rear_motors:
            frame = frame + self.to_chr(motor.speed)
        # distance
        frame = frame + chr(0) + chr(0) + chr(0) + chr(0)
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
            Used to translate a frame received from the STM to update the model

            Model of the frame v.1 :
                >>>  -----------------------------------------------------------
                >>> | 00..00 | Distance | Distance | Distance | Distance | UltrasoundSensors | Battery | AckByte |
                >>> -----------------------------------------------------------

            Model for the battery:
                >>>  ---------------------------------------
                >>> | 0..0 (7 bites) | 0/1 (charged or not) |
                >>>  ---------------------------------------

            :param dataReceived: The received frame
            :type dataReceived: str
        """
        # We transform the received Frame data from hexa to integer
        recvValue = map(ord, dataReceived[1])

        # read distances values
        # ack for initialisation of the distance is the last bit of the byte
        self.model.current_distance = recvValue[3] + recvValue[4]*(2**8)+recvValue[5] * (2**16) + recvValue[6] * (2**24) + self.model.delta_distance
#        print("current distance : "+str(self.model.current_distance))

        # read sensors values
        i = 0
        for sensor in self.model.car.sensors:
            sensor.distance = recvValue[7+i]
            i+=1

        # read battery value
        self.model.car.battery.charged = recvValue[13]
        
        # read ack byte
        self.set_ack_byte(recvValue[14])


    @staticmethod
    def to_chr(n):
        """
            Transform an integer in character

            :param n: the number to Transform
            :type n: int
        """
        if n<0:
            res=256+n
        else:
            res=n
        return chr(res)

    def get_ack_byte(self):
        """
            Return the ack byte according to the different information of the car

            >>> -------------------------------------------------------------
            >>> | 00 | 00 | 00 | 00 | 00 | 00 | reset distance | ack distance |
            >>>  -------------------------------------------------------------

            :return: The ack byte
            :rtype: int
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

            >>>  -------------------------------------------------------------
            >>> | 00 | 00 | 00 | 00 | 00 | 00 | reset distance | ack distance |
            >>>  -------------------------------------------------------------

            :param ack_byte: the ack byte received
            :type ack_byte: int
        """
        # Convert a int in binary number to read each bits separately
        ack_bin = self.dec2bin(ack_byte)
        # update of the ack reset distance bit
        self.model.ack_reset_distance = int(ack_bin[7])
        if(self.model.ack_reset_distance):
            self.model.reset_distance = False

    @staticmethod
    def dec2bin(d,nb=8):
        """
            Transform an interger in string of binary number

            :param d: the integer to transform
            :type d: int
            :param nb: the number of bits to encode the integer
            :type nb: int
        """
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
        """
            Transform a string of binary number in integer

            :param s: the string of binary number
            :type s: str
        """
        return int(s,2)

    def stop(self):
        """
            Allow to stop the thread and quit it
        """
        self.terminated = True
        print("StmController thread closed")
