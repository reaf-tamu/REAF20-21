#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import ms5837
sensor = ms5837.MS5837_02BA()
if not sensor.init():
	exit(1)
def sender():
	pub = rospy.Publisher("Psensor", String, queue_size = 10)
	rospy.init_node("pressure_sensor", anonymous = True)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		data = str(sensor.temperature(ms5837.UNITS_Centigrade))
		rospy.loginfo(data)
		pub.publish(data)
		rate.sleep()
		
if __name__ == "__main__":
	try:
		sender()
	except rospy.ROSInterruptExeception:
		pass
