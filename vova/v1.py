#! /usr/bin/env python
# coding: utf-8

import serial, sys, time, os, os.path, shutil


ser = serial.Serial('/dev/arduino485')
ser.baudrate = 115200
t = 0.05
tt=4

sp1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', ] #'h', 'j', 'k', 'm', ]
SP1 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', ] #'H', 'J', 'M', 'K', ]

def myfun1(aa):
      ser.write(aa)
      time.sleep(t)

def myfun(aa):
      ser.write(aa)
      time.sleep(t)
      print(aa)


while True :

    myfun('O')
    myfun('W')
    myfun('U')
    time.sleep(tt)

    myfun('T')
    myfun('Y')

    myfun('o')
    myfun('w')


    time.sleep(tt)

    myfun('E')

    myfun('u')
    myfun('t')
    time.sleep(tt)


    myfun('U')
    myfun('T')

    myfun('e')
    myfun('y')

    time.sleep(tt)

    myfun('O')
    myfun('W')
    myfun('Q')

    time.sleep(tt)

    myfun('Y')

    myfun('o')
    myfun('u')
    myfun('q')



#    for ii in sp1:
#        myfun1(ii)


    time.sleep(tt)

#    myfun('t')
#    myfun('y')
#    myfun('u')



