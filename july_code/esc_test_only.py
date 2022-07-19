from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
kit.servo[10].angle = 90
kit.servo[8].angle = 90
temp = input("step")
while(True):
	
	angle = int(input("Enter angle: "))
	kit.servo[10].angle = angle
	kit.servo[8].angle = angle
