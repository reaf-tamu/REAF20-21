# !/usr/bin/env python3
import rospy
import message_filters #may need to pip install this onto jetson
from std_msgs.msg import Float32,String

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


if __name__ == '__main__':
  try:
    listener()
  except rospy.ROSInterruptException:
    pass
