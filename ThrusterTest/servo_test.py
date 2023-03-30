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


'''import RPi.GPIO as GPIO
import timeGPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)

servo.angle == 90'''
def set_speed(speed, motor):
	kit.servo[motor].angle = speed
	return

class Motor:
	def __init__(self, name):
		self.name = name
		self.speed = 90
		self.prev_speed = self.speed
	def setSpeed(self, speed):
		self.speed = speed

	def run(self):
		if self.prev_speed != self.speed:
			print("boop")
			kit.servo[self.name].angle = self.speed
			self.prev_speed = self.speed
		else:
			return
	def stop(self):
		kit.servo[name] = 90

A1 = Motor(0)
A2 = Motor(1)
A3 = Motor(2)
A4 = Motor(3)
M1 = Motor(7)
M2 = Motor(9)
M3 = Motor(10)
M4 = Motor(11)

#kit.servo[0].angle = 95
while(1):

	A1.setSpeed(90)
	A1.run()	
	print(A1.speed)
	time.sleep(2)

	#kit.servo[0].angle = 87
	#print(94)
	#time.sleep(5)
