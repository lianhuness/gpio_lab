#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pin1a = 17
pin1b = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin1a, GPIO.OUT)
GPIO.setup(pin1b, GPIO.OUT)


def front():
    print(pin1a)
    print(pin1b)
    GPIO.output(pin1a, True)
    GPIO.output(pin1b, False)

def back():
    GPIO.output(pin1a, False)
    GPIO.output(pin1b, True)

def stop():
    GPIO.output(pin1a, True)
    GPIO.output(pin1b, True)





from distance import getDistance
import time

currentD = 0
while True:
    dis = getDistance()
    print "******Distance = ", dis
    time.sleep(1)
    
    if dis > 20:
        front()
    elif dis > 10:
        back()
    elif dis > 0:
        stop() 
    

    
"""

while True:
    cmd = raw_input("f: forward, b: back, s: stop, e: exit! \n")
    print(cmd)
    if cmd == 'f':
        GPIO.output(pin1a, True)
        GPIO.output(pin1b, False)
    elif cmd == 'b':
        GPIO.output(pin1a, False)
        GPIO.output(pin1b, True)
    elif cmd == 's':
        GPIO.output(pin1a, True)
        GPIO.output(pin1b, True)
    else:
        print(" Bye")
        break        
"""

