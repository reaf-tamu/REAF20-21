#!/usr/bin/env python3
import rospy
#from std_msgs.msg import Float32
from std_msgs.msg import String
from vnpy import *
from math import atan2, pi
import time
import Jetson.GPIO as GPIO


# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BOARD)
# Specify the GPIO pin number you want to read from
pin_number = 18
# Set up the GPIO pin as an input
GPIO.setup(pin_number, GPIO.IN)


mission_switch = False
while mission_switch == False: #checking if mission switch is on
    input_status = GPIO.input(pin_number)
    print(input_status)
    if input_status == GPIO.LOW:
        mission_switch = True #break out of while loop and continue on to the rest of the code
    time.sleep(1)


s = VnSensor()
s.connect("/dev/ttyUSB0",115200)
 
def sender():
	pub = rospy.Publisher('Vnav', String, queue_size=10)
	rospy.init_node('vector_nav', anonymous=True)
	# rate = rospy.Rate(5) # 10hz
	while not rospy.is_shutdown():
#		sensor = s.read_imu_measurements()
#		data_pressure = sensor.pressure
#		rospy.loginfo(data_pressure)
#		pub.publish(data_pressure)
#		rate.sleep()
#		data_gyro = sensor.gyro
#		rospy.loginfo(data_gyro)
#		pub.publish(data_gyro)
#		rate.sleep()
		orientation = s.read_yaw_pitch_roll()
#		x = orientation.x
#		y = orientation.y
#		z = orientation.z
		sensor = s.read_imu_measurements()
		data_pressure = sensor.pressure
		heading = atan2(sensor.mag.x, sensor.mag.y) * 180 / pi
		msg = orientation.x, orientation.y, orientation.z, data_pressure, heading, heading-80
		data = str(msg)
#		data = "X:" + str(x) + ", Y:" + str(y) + ", Z:" + str(z) + ", Pressure:" + str(data_pressure) + ", Heading:" + str(heading)
		rospy.loginfo(data)
#		rospy.loginfo("Reading vNav now: ", orientation.x, orientation.y, orientation.z, data_pressure)
#		msg = orientation.x + " " + orientation.y + " " + orientation.z + " " + data_pressure
		pub.publish(data)
		# rate.sleep()
		time.sleep(1)
         
     
 
if __name__ == '__main__':
	try:
		sender()
	except rospy.ROSInterruptException:
		pass
