#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from distance import getDistance

pin1a = 17
pin1b = 27

pin2a =6 
pin2b =5 

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin1a, GPIO.OUT)
GPIO.setup(pin1b, GPIO.OUT)
GPIO.setup(pin2a, GPIO.OUT)
GPIO.setup(pin2b, GPIO.OUT)


pins = [pin1a, pin1b, pin2a, pin2b] 

b_vals = [True, False, True, False]
f_vals = [False, True, False, True]

s_vals = [False, False, False, False]

l_vals = [True, False, False, True]
r_vals = [False, True, True, False]


   
def front():
    for i in xrange(4):
        GPIO.output(pins[i], f_vals[i])
    
def left():
    for i in xrange(4):
        GPIO.output(pins[i], l_vals[i])

def stop():
    for i in xrange(4):
        GPIO.output(pins[i], s_vals[i])


    
while True:
    cmd = raw_input("f: forward, b: back, s: stop, e: exit! \n")
    print(cmd)
    actions = [] 
    if cmd == 'f':
        print("Start auto mode !!! \n")
        time.sleep(2)
        front()
        while True:
            dis = getDistance()
            print "dis is : ", dis
            if dis > 0 and dis < 10:
                print("... You stoped me.. ")
                stop()
                break
            if dis > 0 and dis < 25:
                stop()
                print(" Find obs. turn left... ")
                time.sleep(1)
                left()
                time.sleep(1)
                print(" front again.. ")
                front()
             
    elif cmd == 's':
        stop() 
    else:
        print(" Bye")
        break        
