import time
from adafruit_servokit import ServoKit
import adafruit_motor.servo

kit = ServoKit(channels = 16)

# Turn OFF all thrusters
A1 = kit.servo[0].angle = 90   
A2 = kit.servo[1].angle = 90   
A3 = kit.servo[2].angle = 90   
A4 = kit.servo[3].angle = 90   
M1 = kit.servo[7].angle = 90    
M2 = kit.servo[9].angle = 90    
M3 = kit.servo[10].angle = 90   
M4 = kit.servo[11].angle = 90    


while(1):
	kit.servo[9].angle = 90
	print(90)
	time.sleep(2)

	#kit.servo[9].angle = 92
	#print(94)
	#time.sleep(5)

'''import RPi.GPIO as GPIO
import timeGPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)

servo.angle == 90'''
