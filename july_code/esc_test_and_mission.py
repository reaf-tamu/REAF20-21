import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time
import board
import digitalio

button = digitalio.DigitalInOut(board.D18)
button.direction = digitalio.Direction.OUTPUT

#GRAY WIRE IN PIN 18!!!!!!

#button.pull = digitalio.Pull.UP
#while(1):
#	print(button.value)
while True:
    button.value = True
    print("True")
    time.sleep(0.5)
    
    button.value = False
    print("False")
    time.sleep(0.5)

#mode = GPIO.getmode()
#print(mode)
#print("hello")
#input_pin = 18
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(input_pin,GPIO.IN)
#GPIO.setup('GPIO12', GPIO.IN)
print("GPIO initiated")

#kit = ServoKit(channels=16)
#kit.servo[8].angle = 90
#kit.servo[10].angle = 90
#temp = input("step")
#value = 0

#try: 
	
	#while(value == 0):
	#	value = GPIO.input(input_pin)
	#	print(value)
	#	angle = int(input("Enter angle: "))
	#	kit.servo[8].angle = angle
	#	kit.servo[10].angle = angle
#finally:
#	GPIO.cleanup()
