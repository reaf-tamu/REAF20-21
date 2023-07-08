import os
from distutils.core import setup, Extension
#import _libvncxx
#import vnpy
import time
from vnpy import *
from math import atan2, pi
import csv

#s = VnSensor()
#s.connect('/dev/ttyUSB0', 115200)
#print(s.read_model_number())
#print(s.read_yaw_pitch_roll())
#reg = s.read_yaw_pitch_roll_magnetic_acceleration_and_angular_rates()
#print(reg.accel)
#s.write_async_data_output_frequency(10)
#s.read_async_data_output_frequency()
#reg = s.read_vpe_basic_control()
#reg.heading_mode
#reg.heading_mode == HEADINGMODE_RELATIVE
#reg.heading_mode = HEADINGMODE_ABSOLUTE
#s.write_vpe_basic_control(reg)
#reg = s.read_vpe_basic_control()
#reg.heading_mode == HEADINGMODE_ABSOLUTE


'''def __main__(self):
        self.pressure = pressure
    def __repr__(self):
        return self.pressure'''
#ez = EzAsyncData()
#ez.connect('/dev/ttyUSB0', 115200)
#ez = EzAsyncData.connect('/dev/ttyUSB0', 115200)
#cd = ez.current_data
#p = CompositeData()
#p.connect('/dev/ttyUSB0', 115200)
#print(ez.temperature)

s = VnSensor()
s.connect('/dev/ttyUSB0', 115200)

"""
#import csv
while(True):
	with open('vn100.csv','w') as f:
		orientation = s.read_yaw_pitch_roll()
		writer = csv.writer(f)
		row = [orientation.x]
		writer.writerow(row)
		print(row)
	time.sleep(10)
"""

#orientation = s.read_yaw_pitch_roll()
#print(f"x axis: {orientation.x}\ny axis {orientation.y}\nz axis {orientation.z}")
#minute = 0
#while minute <= 5:
#	time.sleep(60)
#	minute += 1
#	print(minute)
#print("")

#seconds = 0
#with open('vn100_heading_yaw.csv','w') as f:

while(True):
	orientation = s.read_yaw_pitch_roll()
#	print(f"x axis: {orientation.x}\ny axis: {orientation.y}\nz axis: {orientation.z}")
	print("x axis:", {orientation.x},"\ny axis:",{orientation.y},"\nz axis:",{orientation.z})
	imuData = s.read_imu_measurements()
	print(imuData.pressure," kPa")
#		print(imuData.mag," Gaus")		
	heading = atan2(imuData.mag.x, imuData.mag.y) * 180 / pi
	new_heading = heading - 60	
	print(new_heading)
	print(heading)
#		print(YawPitchRollMagneticAccelerationAndAngularRatesRegister.mag)
#		print(imuData.accel," m/s^2")
#		print(imuData.gyro," rad/s")
#		print(imuData.temp," C")
	print('\n\n')
	time.sleep(5)

#	seconds += 1	

#		writer = csv.writer(f)
		#row = [seconds, orientation.x, orientation.y, orientation.z, imuData.pressure, new_heading]
#		row = [seconds, orientation.x, new_heading, heading]
#		writer.writerow(row)
#m = ImuMeasurementsRegister
#s.connect('/dev/ttyUSB0', 115200)
#cd = ez.current_data
#p = CompositeData()
#p.connect('/dev/ttyUSB0', 115200)
#print(s.read_imu_measurements())

#s = VnSensor()
#s.connect('/dev/ttyUSB0', 115200)
#c = GpsCompassBaselineRegister()
#print(s.read_gps_compass_baseline())




#class CompositeData:
#    attr1 = CompositeData.any_pressure
#print(CompositeData().attr1)
#print(CompositeData(0x7fd7dbd7cb80))
#x = CompositeData.pressure
#print(x)
#print(CompositeData())



#ez.sensor.write_async_data_output_frequency(1)
#print(ez.sensor.read_async_data_output_frequency())
