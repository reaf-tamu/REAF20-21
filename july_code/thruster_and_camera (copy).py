import numpy as np
import cv2
from adafruit_servokit import ServoKit
import time

input2 = input("Enter video name:")
cap = cv2.VideoCapture(0)
kit = ServoKit(channels=16)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(input2+'.mp4', fourcc, 20.0, (640, 480))

mission = 0
sleep_sec = 1

move = input("Enter: [w]Forward [a]Left [d]Right [q]Slight Left [e] Slight Right")

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
	servo = kit.servo[15].angle = val8	#

#While(mission = 1)#While the mission switch is not 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)

        if (move == "w"):
            thruster_val(96,90,96,90,96,90,97,90)
            print("Forward")
            time.sleep(sleep_sec)
            stop()

        elif(move =="d"):
            thruster_val(90,90,90,90,96,90,97,90)
            print("Right")
            time.sleep(sleep_sec)
            stop()

        elif(move =="d"):
            thruster_val(96,90,96,90,90,90,90,90)
            print("Left")
            time.sleep(sleep_sec)
            stop()

        elif(move =="e"):
            #Same values as Left, time reduced by half
            thruster_val(90,90,90,90,96,90,97,90)
            print("Slight Right")
            time.sleep(sleep_sec/2)
            stop()

        elif(move =="q"):
            #Same values as Right, time reduced by half
            thruster_val(96,90,96,90,90,90,90,90)
            print("Slight Left")
            time.sleep(sleep_sec/2)
            stop()

        elif(move =="p"):
            #Same values as Right, time reduced by half
            thruster_val(90,90,90,90,90,90,90,90)
            print("Servo")
            time.sleep(sleep_sec/2)
            stop()
            thruster_val(90,90,90,90,96,90,90,0)
            time.sleep(sleep_sec/2)
            stop()

        else:
            thruster_val(90,90,90,90,90,90,90,90)
            print("Waiting = Stop")
            time.sleep(sleep_sec)
            stop()

    move = input("Enter: [w]Forward [a]Left [d]Right [q]Slight Left [e] Slight Right")

cap.release()
out.release()
cv2.destroyAllWindows()
