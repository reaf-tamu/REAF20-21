#!/usr/bin/env python3
import rospy
#from std_msgs.msg import Float32
from std_msgs.msg import String
from vnpy import *

s = VnSensor()
s.connect(‘/dev/ttyUSB0’,115200)
 
def sender():
     pub = rospy.Publisher('Vnav', String, queue_size=10)
     rospy.init_node('vector_nav', anonymous=True)
     rate = rospy.Rate(5) # 10hz
     while not rospy.is_shutdown():
#          sensor = s.read_imu_measurements()
#          data_pressure = sensor.pressure
#          rospy.loginfo(data_pressure)
#          pub.publish(data_pressure)
#          rate.sleep()
         
#          data_gyro = sensor.gyro
#          rospy.loginfo(data_gyro)
#          pub.publish(data_gyro)
#          rate.sleep()
         orientation = s.read_yaw_pitch_roll()
         sensor = s.read_imu_measurements()
         data_pressure = sensor.pressure
         rospy.loginfo("Reading vNav now: ", orientation.x, orientation.y, orientation.z, data_pressure)
         msg = orientation.x + " " + orientation.y + " " + orientation.z + " " + data_pressure 
         pub.publish(msg)
         rate.sleep()
         
     
 
 if __name__ == '__main__':
     try:
         sender()
     except rospy.ROSInterruptException:
         pass
