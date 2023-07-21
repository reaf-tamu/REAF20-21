#!/user/bin/env python3
import rospy
import Jetson.GPIO as GPIO
import time
from adafruit_servokit import ServoKit
# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BOARD)

# Specify the GPIO pin number you want to read from
pin_number = 18

# Set up the GPIO pin as an input
GPIO.setup(pin_number, GPIO.IN)

TARGET_DEPTH = 5 #adjust this constant as needed
ping = 0
vnav = 0
pressure = 0
mission_switch = False
def vn_callback(data):
    #	rospy.loginfo(rospy.get_caller_id() + " heard %s", data.data)
    global vnav
    vnav = data.data
def ping_callback(data):
    #	rospy.loginfo(rospy.get_caller_id() + " heard %s", data.data)
    global ping
    ping = float(data.data)
def pressure_callback(data):
    #	rospy.loginfo(rospy.get_caller_id() + " heard %s", data.data)
    global pressure
    pressure = float(data.data)

def helper_get_depth(pinger, ps): #FIX_ME
    #vehicle_heigth is height of AUV
    #manually change pool_depth and vehicle_height
    pinger_value = pool_depth - pinger - (vehicle_height / 2)
    ps_value = ps + (vehicle_height / 2)
    average = (pinger_value + ps_value) / 2
    return average

while not mission_switch: #checking if mission switch is on
    input_status = GPIO.input(pin_number)
    if input_status == GPIO.LOW:
        mission_switch = True #break out of while loop and continue on to the rest of the code
    time.sleep(1)

rospy.init_node("listener", anonymous=True)

# initiating thrusters
kit = ServoKit(channels = 16)

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

while not rospy.is_shutdown():
    rospy.Subscriber("Pinger", Float32, ping_callback)
    rospy.Subscriber("Vnav", String, vn_callback)
    rospy.Subscriber("Pressure", String, pressure_callback)

    #vertical movement
    cur_depth = helper_get_depth(ping, pressure)
    if (cur_depth < TARGET_DEPTH): #go down if above target depth
        A2.setSpeed(100); A4.setSpeed(100); M2.setSpeed(100); M4.setSpeed(100)
        A2.run(); A4.run(); M2.run(); M4.run()
    else:
        A2.setSpeed(90);A4.setSpeed(90);M2.setSpeed(90);M4.setSpeed(90)
        A2.run();A4.run();M2.run();M4.run()

    #horizontal movement
    yaw = float(vnav[4]) #adjust the index of the vnav tuple as needed

    rospy.sleep(3)