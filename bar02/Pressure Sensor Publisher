import rospy
from Pressure_Sensor import Pressure_Sensor
from std_msgs.msg import Float32

freshwaterDepth, saltwaterDepth, chlorinewaterDepth = Pressure_Sensor

def talker():
  pub = rospy.Publisher('Pressure Sensor', Float32, queue_size=10)
  rospy.init_node('bar02', anonymous=True)
  rate = rospy.Rate(10) #10 Hz
  while not rospy.is_shutdown():
    Depth = freshwaterDepth #Change to type of water #Depth is in meters
    rospy.loginfo(Depth)
    pub.publish(Depth)
    rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
