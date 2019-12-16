import RPi.GPIO as GPIO
import time

pin_id = 12
sleep_time = 0.25

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_id, GPIO.OUT) 

def flash(pin_id, sleep_time):
    try:
        while True:
            GPIO.output(pin_id, GPIO.HIGH)
            time.sleep(sleep_time)
            GPIO.output(pin_id, GPIO.LOW)
            time.sleep(sleep_time)
    except KeyboardInterrupt:
       return

def main():
    flash(pin_id, sleep_time)
    GPIO.cleanup()

if __name__ == "__main__":
    # execute only if run as a script
    main()
