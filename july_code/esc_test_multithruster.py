from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
kit.servo[0].angle = 90
kit.servo[10].angle = 90
kit.servo[3].angle = 90
kit.servo[12].angle = 90
temp = input("step")
while(True):
	#trying to make thrusters move at different speeds
	angle1 = int(input("Enter angle1: "))
	angle2 = int(input("Enter angle2: "))
	angle3 = int(input("Enter angle3: "))
	angle4 = int(input("Enter angle4: "))
	kit.servo[0].angle = angle1
	kit.servo[10].angle = angle2
	kit.servo[3].angle = angle3
	kit.servo[12].angle = angle4
