#! /usr/bin/env python
# coding: utf-8

import serial, sys, time

ser = serial.Serial("/dev/arduino485")
ser.baudrate = 115200

tt = 0.5

while True :
  ser.write('I')
  ser.write('D')
  ser.write('F')
  time.sleep(5) #4 min


  ser.write('i')
  ser.write('d')
  ser.write('f')
  time.sleep(0.5)
  ser.write('I')
  ser.write('D')
  ser.write('F')
  time.sleep(1.5)


  ser.write('i')
  ser.write('d')
  ser.write('f')
  time.sleep(0.9)
  ser.write('I')
  ser.write('D')
  ser.write('F')
  time.sleep(1)

  ser.write('i')
  ser.write('d')
  ser.write('f')
  time.sleep(3)
  ser.write('I')
  time.sleep(0.1)
  ser.write('i')
  ser.write('D')
  time.sleep(0.3)
  ser.write('d')
  ser.write('F')
  time.sleep(0.5)
  ser.write('f')
  time.sleep(5)



