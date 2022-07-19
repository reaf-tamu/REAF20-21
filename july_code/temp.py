import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time

mode = GPIO.getmode()
print(mode)
