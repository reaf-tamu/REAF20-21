import rospy
from std_msgs.msg import Float32

def callback(data):
    rospy.loginfo("Recieved Data: %f", data.data)

def listener():
    rospy.init_node('Subscriber_Node', anonymous=True)
    rospy.Subscriber("Pinger", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
  try:
    listener()
  except rospy.ROSInterruptException:
    pass
