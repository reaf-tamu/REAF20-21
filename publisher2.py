# !/usr/bin/env python3
# license removed for brevity
#woudl contain vector nav and zed mini
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('sub2', String, queue_size=10)
    rospy.init_node('pub2', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        hello_str = "publisher2" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
