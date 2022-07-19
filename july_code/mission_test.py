import RPi.GPIO as GPIO
import time

input_pin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(input_pin,GPIO.IN)
print("GPIO initiated")
try:
	while True:
		value = GPIO.input(input_pin)
		print(value)
		time.sleep(1)
finally:
	GPIO.cleanup()
