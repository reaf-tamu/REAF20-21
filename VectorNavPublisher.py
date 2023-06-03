#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from vnpy import *

s = VnSensor()
s.connect(‘/dev/ttyUSB0’,115200)
 
def sender():
     pub = rospy.Publisher('Vnav', Float32, queue_size=10)
     rospy.init_node('vector_nav', anonymous=True)
     rate = rospy.Rate(5) # 10hz
     while not rospy.is_shutdown():
         sensor = s.read_imu_measurements()
         data_pressure = sensor.pressure
         rospy.loginfo(data_pressure)
         pub.publish(data_pressure)
         rate.sleep()
         
         data_gyro = sensor.gyro
         rospy.loginfo(data_gyro)
         pub.publish(data_gyro)
         rate.sleep()
 
 if __name__ == '__main__':
     try:
         sender()
     except rospy.ROSInterruptException:
         pass
