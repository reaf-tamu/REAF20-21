#!/usr/bin/env python3
import rospy
#from std_msgs.msg import Float32
from std_msgs.msg import String
from vnpy import *
from math import atan2, pi
import time

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
		data = "Vnav: " + str(msg)
#		data = "X:" + str(x) + ", Y:" + str(y) + ", Z:" + str(z) + ", Pressure:" + str(data_pressure) + ", Heading:" + str(heading)
		rospy.loginfo(data)
#		rospy.loginfo("Reading vNav now: ", orientation.x, orientation.y, orientation.z, data_pressure)
#		msg = orientation.x + " " + orientation.y + " " + orientation.z + " " + data_pressure
		pub.publish(data)
		# rate.sleep()
		time.sleep(10)
         
     
 
if __name__ == '__main__':
	try:
		sender()
	except rospy.ROSInterruptException:
		pass
