#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from brping import Ping1D
myPing = Ping1D()
myPing.connect_serial("COM3", 115200)
if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)

def sender():
    pub = rospy.Publisher('Pinger', Float32, queue_size=10)
    rospy.init_node('sonar', anonymous=True)
    rate = rospy.Rate(5)  # 10hz
    while not rospy.is_shutdown():
        data = myPing.get_distance_simple()
        data = data['distance'] * (10 ** -3) #convert to meters
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        sender()
    except rospy.ROSInterruptException:
        pass
