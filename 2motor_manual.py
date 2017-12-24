#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

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


   

    

while True:
    cmd = raw_input("f: forward, b: back, s: stop, e: exit! \n")
    print(cmd)
    actions = [] 
    if cmd == 'f':
        actions = f_vals 
    elif cmd == 'b':
        actions = b_vals 
    elif cmd == 'l':
        actions = l_vals
    elif cmd == 'r':
        actions = r_vals
    elif cmd == 's':
        actions = s_vals    
    else:
        print(" Bye")
        break        
    
    for i in xrange(4):
        GPIO.output(pins[i], actions[i])
