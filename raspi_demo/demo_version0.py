#!/usr/bin/python
# servo control example
# Connection
# Black - GND (pin 6)
# Red   - 3.3V (pin 1)
# Yellow/Orange - GPIO18 (pin 12)

import RPi.GPIO as GPIO
import time
import calendar

import cv2
import numpy as np

# servoPIN = 18
servoPIN = 16
GPIO.setmode(GPIO.BCM)

# light pins
redPIN = 18
greenPIN = 23
bluePIN = 24
def lightOn(pin_id):
    GPIO.setup(pin_id, GPIO.OUT)
    GPIO.output(pin_id, GPIO.HIGH)
    
def lightOff(pin_id):
    GPIO.setup(pin_id, GPIO.OUT)
    GPIO.output(pin_id, GPIO.LOW)

def redLightOn():
    lightOn(redPIN)

def redLightOff():
    lightOff(redPIN)

def greenLightOn():
    lightOn(greenPIN)

def greenLightOff():
    lightOff(greenPIN)

def blueLightOn():
    lightOn(bluePIN)

def blueLightOff():
    lightOff(bluePIN)

GPIO.setup(servoPIN, GPIO.OUT)

def demo():
    cap = cv2.VideoCapture(0)

    p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
    p.start(2.5) # Initialization

    cycles = [2.5, 5, 7.5, 10, 12.5, 10, 7.5, 5, 2.5]

    for cycle in cycles:
        p.ChangeDutyCycle(cycle)
        time.sleep(0.5)
    
    p.stop()

    count = 0
    try:
        while True:
            ret, frame = cap.read()
            if ret:
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                h = hsv[:,:,0]
                s = hsv[:,:,1]
                v = hsv[:,:,2]
                print h.mean(), s.mean(), v.mean()
                fname = "img_{}.jpg".format(calendar.timegm(time.gmtime()));
                print fname
                if count % 5 == 0:
                  cv2.imwrite(fname, frame)
                time.sleep(1)
                count = count + 1

    except KeyboardInterrupt:
        GPIO.cleanup()
        p.stop()
        cap.release()
    else:
        GPIO.cleanup()
        p.stop()
        cap.release()

def main():
    demo()

if __name__ == "__main__":
    # execute only if run as a script
    main()
