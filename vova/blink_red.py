#! /usr/bin/env python
# coding: utf-8

import serial, sys, time

ser = serial.Serial("/dev/arduino485")
ser.baudrate = 115200

tt = 0.5

while True :
  ser.write('p')
  ser.write('g')

  time.sleep(1)
  ser.write('P')
  ser.write('G')
  time.sleep(2)

