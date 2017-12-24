#! /usr/bin/env python
# coding: utf-8

import serial, sys, time

ser = serial.Serial("/dev/arduino485")
ser.baudrate = 115200

tt = 0.5

while True :
  ser.write('s')
  time.sleep(3)
  ser.write('S')
  time.sleep(2)

