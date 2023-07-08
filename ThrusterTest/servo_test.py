import time
from adafruit_servokit import ServoKit
#import adafruit_motor.servo
#import keyboard

kit = ServoKit(channels = 16)

# Turn OFF all thrusters
A1 = kit.servo[0].angle = 90   
A2 = kit.servo[1].angle = 90   
A3 = kit.servo[2].angle = 90   
A4 = kit.servo[3].angle = 90   
M1 = kit.servo[7].angle = 90    
M2 = kit.servo[9].angle = 90    
M3 = kit.servo[10].angle = 90   
M4 = kit.servo[13].angle = 90    


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
M4 = Motor(13)

M4.setSpeed(90)
M4.run()
M3.setSpeed(90)
M3.run()
M2.setSpeed(90)
M2.run()
M1.setSpeed(90)
M1.run()
A4.setSpeed(90)
A4.run()
A3.setSpeed(90)
A3.run()
A2.setSpeed(90)
A2.run()
A1.setSpeed(90)
A1.run()

#time.sleep(180)

#kit.servo[0].angle = 95
while(1):

# left/right
	A3.setSpeed(90)
	A3.run()	
	print('A3 =',A3.speed)
	#time.sleep(2)

# left/right
	M1.setSpeed(90)
	M1.run()	
	print('M1 =',M1.speed)
#	time.sleep(2)
	
	# left/right
	A1.setSpeed(90)
	A1.run()	
	print('A1 =',A1.speed)
#	time.sleep(2)

	# up/down
	A2.setSpeed(90)
	A2.run()	
	print('A2 =',A2.speed)
#	time.sleep(2)


	# up/down
	A4.setSpeed(90)
	A4.run()	
	print('A4 =',A4.speed)
#	time.sleep(2)

	
	# up/down
	M2.setSpeed(90)
	M2.run()	
	print('M2 =',M2.speed)
#	time.sleep(2)

# left/right
	M3.setSpeed(90)
	M3.run()	
	print('M3 =',M3.speed)
	#time.sleep(2)

	# up/down
	M4.setSpeed(90)
	M4.run()	
	print('M4 =',M4.speed)
#	time.sleep(2)
	
	print("\n\n")
"""
	if keyboard.read_key() == "q":
		print("hey we did it")
		break
"""
	

	#kit.servo[0].angle = 87
	#print(94)
	#time.sleep(5)
