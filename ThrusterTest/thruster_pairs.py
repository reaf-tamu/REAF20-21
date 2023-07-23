import time
from adafruit_servokit import ServoKit
#import Jetson.GPIO as GPIO
import digitalio
import board
#import adafruit_motor.servo
#import keyboard


button = digitalio.DigitalInOut(board.D18)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while (1):
    status = button.value
    print(status)
    time.sleep(1)


"""
# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BOARD)
# Specify the GPIO pin number you want to read from
pin_number = 18
# Set up the GPIO pin as an input
GPIO.setup(pin_number, GPIO.IN)

while True:
	input_status = GPIO.input(pin_number)
	print(input_status)
	time.sleep(1)
"""


#kit = ServoKit(channels = 16, address = 0x40)

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



mission_switch = False


# test forward movement
while mission_switch == False: #checking if mission switch is on
    input_status = GPIO.input(pin_number)
    print(input_status)
    if input_status == GPIO.LOW:
        mission_switch = True #break out of while loop and continue on to the rest of the code
    time.sleep(1)

# time to go
while mission_switch == True:

    #run thrusters
    M3.setSpeed(100)
    A1.setSpeed(100)
    M3.run()
    A1.run()

    # check status
    input_status = GPIO.input(pin_number)
    if input_status == GPIO.HIGH:
        mission_switch = False
        #stop thrusters
        M3.setSpeed(90)
        A1.setSpeed(90)
        M3.run()
        A1.run()



# test backward movement
while mission_switch == False: #checking if mission switch is on
    input_status = GPIO.input(pin_number)
    if input_status == GPIO.LOW:
        mission_switch = True #break out of while loop and continue on to the rest of the code
    time.sleep(1)

# time to go
while mission_switch == True:

    #run thrusters
    M1.setSpeed(100)
    A3.setSpeed(100)
    M1.run()
    A3.run()

    # check status
    input_status = GPIO.input(pin_number)
    if input_status == GPIO.HIGH:
        mission_switch = False
        #stop thrusters
        M1.setSpeed(90)
        A3.setSpeed(90)
        M1.run()
        A3.run()



# test up movement
while mission_switch == False: #checking if mission switch is on
    input_status = GPIO.input(pin_number)
    if input_status == GPIO.LOW:
        mission_switch = True #break out of while loop and continue on to the rest of the code
    time.sleep(1)

# time to go
while mission_switch == True:

    #run thrusters
    M4.setSpeed(100)
    A2.setSpeed(100)
    M4.run()
    A2.run()

    # check status
    input_status = GPIO.input(pin_number)
    if input_status == GPIO.HIGH:
        mission_switch = False
        #stop thrusters
        M4.setSpeed(90)
        A2.setSpeed(90)
        M4.run()
        A2.run()



# test down movement
while mission_switch == False: #checking if mission switch is on
    input_status = GPIO.input(pin_number)
    if input_status == GPIO.LOW:
        mission_switch = True #break out of while loop and continue on to the rest of the code
    time.sleep(1)

# time to go
while mission_switch == True:

    #run thrusters
    M2.setSpeed(100)
    A4.setSpeed(100)
    M2.run()
    A4.run()

    # check status
    input_status = GPIO.input(pin_number)
    if input_status == GPIO.HIGH:
        mission_switch = False
        #stop thrusters
        M2.setSpeed(90)
        A4.setSpeed(90)
        M2.run()
        A4.run()
