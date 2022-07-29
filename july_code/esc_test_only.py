from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
#kit.servo[10].angle = 90
#kit.servo[8].angle = 90
#temp = input("step")
#while(True):
	
#	angle = int(input("Enter angle: "))
#	kit.servo[10].angle = angle
#	kit.servo[8].angle = angle

mission = 0
sleep_sec = 5

move = input("Enter: [W]Forward [A]Left [D]Right [Q]Slight Left [E] Slight Right")

def stop():
	thruster_val(90,90,90,90,90,90,90,90)
	print("Stop")

def thruster_val(val1, val2, val3, val4, val5, val6, val7, val8):
	A1 = kit.servo[0].angle = val1	#
	A2 = kit.servo[1].angle = val2	#
	A3 = kit.servo[2].angle = val3	#
	A4 = kit.servo[3].angle = val4	#
	M1 = kit.servo[7].angle = val5	#
	M2 = kit.servo[9].angle = val6	#
	M3 = kit.servo[10].angle = val7	#
	M4 = kit.servo[11].angle = val8	#

#While(mission = 1)#While the mission switch is not 0
while (1):
	if (move == "W"):
		thruster_val(96,90,96,90,96,90,96,90)
		print("Forward")
		time.sleep(sleep_sec)
		stop()

	elif(move =="A"):
		thruster_val(90,90,90,90,96,90,96,90)
		print("Left")
		time.sleep(sleep_sec)
		stop()

	elif(move =="D"):
		thruster_val(96,90,96,90,90,90,90,90)
		print("Right")
		time.sleep(sleep_sec)
		stop()

	elif(move =="Q"):
		#Same values as Left, time reduced by half
		thruster_val(90,90,90,90,96,90,96,90)
		print("Slight Left")
		time.sleep(sleep_sec/2)
		stop()

	elif(move =="E"):
		#Same values as Right, time reduced by half
		thruster_val(96,90,96,90,90,90,90,90)
		print("Slight Right")
		time.sleep(sleep_sec/2)
		stop()

	else:
		thruster_val(90,90,90,90,90,90,90,90)
		print("Waiting = Stop")
		time.sleep(sleep_sec)
		stop()

	move = input("Enter: [W]Forward [A]Left [D]Right [Q]Slight Left [E] Slight Right")

