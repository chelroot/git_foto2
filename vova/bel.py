#! /usr/bin/env python
# coding: utf-8

import serial, sys, time

ser = serial.Serial("/dev/arduino485")
ser.baudrate = 115200

tt = 0.5

while True :
  ser.write('a')

 # time.sleep(240)
  time.sleep(5)
  ser.write('A')
#  time.sleep(60)
  time.sleep(5)

