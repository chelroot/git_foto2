#! /usr/bin/env python
# coding: utf-8

import serial, sys, time, os, os.path, shutil


ser = serial.Serial('/dev/arduino485')
ser.baudrate = 115200
t = 0.02
tt=1

sp1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', ] #'h', 'j', 'k', 'm', ]
SP1 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', ] #'H', 'J', 'M', 'K', ]



def myfun(aa):
      ser.write(aa)
      time.sleep(t)
for ii in SP1:
    myfun(ii)

print('Все включил')
