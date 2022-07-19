import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time

mode = GPIO.getmode()
print(mode)

input_pin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(input_pin,GPIO.IN)
print("GPIO initiated")

kit = ServoKit(channels=16)
kit.servo[8].angle = 90
kit.servo[10].angle = 90
temp = input("step")
value = 0

try: 
	while(value == 0):
		value = GPIO.input(input_pin)
		print(value)
		angle = int(input("Enter angle: "))
		kit.servo[8].angle = angle
		kit.servo[10].angle = angle
finally:
	GPIO.cleanup()
