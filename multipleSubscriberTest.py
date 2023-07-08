#!/usr/bin/env python3
import rospy
import message_filters #may need to pip install this onto jetson
from std_msgs.msg import Float32,String


# this code have different callback functions for each sensor. This allows us to set them as global variables
# it works with pinger as is
# variable vnav is a string and will need to be parsed to compare to values

ping = 0
vnav = 0
pressure = 0

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
	pressure = data.data

rospy.init_node("listener", anonymous = True)

while not rospy.is_shutdown():
	rospy.Subscriber("Pinger", Float32, ping_callback)
	rospy.Subscriber("Vnav", String, vn_callback)
	rospy.Subscriber("Pressure", String, pressure_callback)
	rospy.sleep(3)
	
	print(pressure)
"""	
	print(ping)
	
	if ping > 0.0:
		print("True")
	else:
		print("False")
"""

"""
This is Erin's new data. She said to switch it to more simple

def callback(sonar,vN):
    rospy.loginfo("Received sonar data: %f", sonar.data)
    rospy.loginfo("Received vector Nav data: %f", vN.data)

def listener():
    sonar = message_filters.Subscriber("Pinger", Float32)
    sonar.registerCallback(callback)
    vectorNav = message_filters.Subscriber("Vnav", String)
    vectorNav.registerCallback(callback)
    rospy.init_node('Multiple_Subscriber_Node', anonymous=True)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
"""
"""
This is the simple code copied and adjusted from test_listener.py

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + " heard %s", data.data)
	
def listener():
	rospy.init_node("listener", anonymous = True)
	rospy.Subscriber("Vnav", String, callback)
	rospy.Subscriber("Pinger", String, callback)

	rospy.spin()

if __name__ == '__main__':
  try:
    listener()
  except rospy.ROSInterruptException:
    pass
"""

