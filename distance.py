#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

MAX_WAIT_HC_SR04_COUNTER =  65530  


def getDistance():

# BOARD / BCM mode 
    GPIO.setmode(GPIO.BCM)

#set GPIO Pins 

    TRIG = 23
    ECHO = 24

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    cnt = 10
    pre = 3
   
    output = [] 
    while cnt >= 0:
        GPIO.output(TRIG, False)  # Set TRIG as LOW 
        
        GPIO.output(TRIG, True) # Set Trig as HIGH
        time.sleep(0.00001) # Delay of 0.0001 seconds
        GPIO.output(TRIG, False)    # TRIG as LOW
        
        WAIT_CNT = 0         
        while GPIO.input(ECHO) == 0 and WAIT_CNT < MAX_WAIT_HC_SR04_COUNTER:
            pulse_start = time.time()
            WAIT_CNT = WAIT_CNT+1
        
        if WAIT_CNT == MAX_WAIT_HC_SR04_COUNTER:
            print(" \n\n ***** ERROR , HIT DISTANCE WAIT MAXIMUM **** \n\n ")
            return 0 

        WAIT_CNT = 1
        pulse_end = 0
        while GPIO.input(ECHO) == 1 and WAIT_CNT < MAX_WAIT_HC_SR04_COUNTER:
            pulse_end = time.time()
            WAIT_CNT = WAIT_CNT+1
    
        if WAIT_CNT == MAX_WAIT_HC_SR04_COUNTER:
            print(" \n\n ***** ERROR , HIT DISTANCE WAIT MAXIMUM **** \n\n ")
            return 0 
        pulse_duration = pulse_end - pulse_start
    
 
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        distance = distance-0.5   # 0.5 calibration

#        if distance > 2 and distance < 400:
            #print "Distance: ", distance, "cm"
#        else:
#            print "Out of Range"
        
        if pre <= 0:
            output.append(distance) 
        pre = pre-1
        cnt = cnt - 1
    aveDis = reduce(lambda x, y: x+y, output)/len(output)
    return round(aveDis,2)

#import pdb
#dis = getDistance()
#print(dis)
