import os 
from distutils.core import setup, Extension
import time
from vnpy import *
from math import atan, pi
import csv
from datetime import datetime

s=VnSensor()
s.connect('/dev/ttyUSB1',115200)

orientation = s.read_yaw_pitch_roll()
imuData = s.read_imu_measurements()

header = ['x','y','z','Pressure']

with open('vectornav_'+str(datetime.now())+'.csv','w') as file:
	writer = csv.writer(file)
	writer.writerow(header)
	while(True):
		data = [orientation.x, orientation.y, orientation.z,imuData.pressure]
		writer.writerow(data)
		time.sleep(1)
