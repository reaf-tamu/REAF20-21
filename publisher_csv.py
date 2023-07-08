#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32, String
import csv
import time

# vectornav csv
"""
def talker():
	pub = rospy.Publisher("CSV", String, queue_size=10)
	rospy.init_node("press_sens", anonymous = True)
	while not rospy.is_shutdown():
		with open('/home/reafauv2017/Desktop/auv/REAF20-21/vn100/vn100.csv', 'r') as file:
			reader =  csv.reader(file)
			for row in reader:
				data = str(row[0])
				rospy.loginfo(data)
				pub.publish(data)
		time.sleep(10)
"""

# pressure sensor csv
# need to connect pressure sensor
def talker():
	pub = rospy.Publisher("Pressure", String, queue_size=10)
	rospy.init_node("pressure_sensor", anonymous = True)
	while not rospy.is_shutdown():
		with open('/home/reafauv2017/Desktop/auv/REAF20-21/bar02/pressure_sensor_pub.csv', 'r') as file:
			reader =  csv.reader(file)
			for row in reader:
				data = str(row)
				rospy.loginfo(data)
				pub.publish(data)
		time.sleep(10)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
