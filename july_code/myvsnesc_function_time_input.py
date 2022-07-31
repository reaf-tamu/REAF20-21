from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
mission = 0

# delays created with 15.5 lbs of scuba weights


###FUNCTIONS#####
def stop():
	# Stop (duh)
	thruster_val(90,90,90,90,90,90,90,90)
	print("Stop")

def thruster_val(val1, val2, val3, val4, val5, val6, val7, val8):
	A1 = kit.servo[0].angle = val1	# 90+ (forward)
	A2 = kit.servo[1].angle = val2	# 90- (up)
	A3 = kit.servo[2].angle = val3	# 90- (backward, stutters)
	A4 = kit.servo[3].angle = val4	# 90+ (down)
	M1 = kit.servo[7].angle = val5	# 90- (backward, stutters)
	M2 = kit.servo[9].angle = val6	# 90+ (down)
	M3 = kit.servo[10].angle = val7	# 90+++ (forward, WEAK, sometimes doesn't work)
	M4 = kit.servo[12].angle = val8	# 90+ (down)

def right(timeright):
	# Turn right
	thruster_val(94,90,84.5,90,90,90,90,90)
	print("Right")
	time.sleep(timeright)

def left():
	# Turn left
	thruster_val(90,90,90,90,84.5,90,97,90)
	print("Left")
	time.sleep(1)

def forward(timeforward):
	# Go forward
	thruster_val(97.2,90,78,90,77,90,104,90)
	print("Forward")
	time.sleep(timeforward)

def down(timedown):
	# Go down
	thruster_val(90,80,90,98,90,98,90,98)
	print("Down")
	time.sleep(timedown) # test 20 for larger pool

def donut(timedonut): # try this
	# Left point turn
	thruster_val(84,90,102,90,76,90,107,90)
	print("Donut")
	time.sleep(timedonut)

###PROGRAM###
down(8)
forward(3.5)
down(4)
forward(3.5)
down(4)
forward(3.5)
down(4)
donut(32)
stop()
stop()
