
import Jetson.GPIO as GPIO
import time

# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BOARD)

# Specify the GPIO pin number you want to read from
pin_number = 18

# Set up the GPIO pin as an input
GPIO.setup(pin_number, GPIO.IN)

try:
    while True:
        # Read the input status
        input_status = GPIO.input(pin_number)
        
        # Check the input status and perform actions accordingly
        if input_status == GPIO.HIGH:
            print("Input is HIGH")
        elif input_status == GPIO.LOW:
            print("Input is LOW")

        time.sleep(1)
        
except KeyboardInterrupt:
    # Clean up the GPIO settings on program exit
    GPIO.cleanup()



"""
import Jetson.GPIO as GPIO
import time
import os

# adjust pin number
buttonpin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonpin,GPIO.IN)

# while True:

for range(5):
	try:
		if (GPIO.input(buttonpin)):
			os.system("python3 vn100/vn100_code.py")
	except:
		break
"""
