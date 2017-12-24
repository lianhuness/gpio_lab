#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# BOARD / BCM mode 
GPIO.setmode(GPIO.BCM)

#set GPIO Pins 

TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

while True:
    GPIO.output(TRIG, False)  # Set TRIG as LOW 
    print "Waiting for sensor to settle"
    #time.sleep(2)   # Delay of 2 seconds

    GPIO.output(TRIG, True) # Set Trig as HIGH
    time.sleep(0.00005) # Delay of 0.0001 seconds
    GPIO.output(TRIG, False)    # TRIG as LOW

    t1= time.time()
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        t2 = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        t3 = time.time()
     
    pulse_duration = pulse_end - pulse_start
    
 
    print "t1: ", t1, "  T2:", t2, "  t3:", t3
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    if distance > 2 and distance < 400:
        print "Distance: ", distance-0.5, "cm"
    else:
        print "Out of Range"

