# servo control example
# Connection
# Black - GND (pin 6)
# Red   - 3.3V (pin 1)
# Yellow/Orange - GPIO18 (pin 12)

import RPi.GPIO as GPIO
import time

# servoPIN = 18
servoPIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(2.5) # Initialization
count = 0
try:
  # while True:
  while count < 1:
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    count = count + 1
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
p.stop()
GPIO.cleanup()
