import numpy as np
import cv2
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
sleep_sec = 1

print(""AUV Single Motor Test Begin:)
move = input("Begin input:")

def stop():
    thruster_val(90,90,90,90,90,90,90,90)
    print("Stop")

def thruster_val(val1, val2, val3, val4, val5, val6, val7, val8):
    A1 = kit.servo[0].angle = val1    #
    A2 = kit.servo[1].angle = val2    #
    A3 = kit.servo[2].angle = val3    #
    A4 = kit.servo[3].angle = val4    #
    M1 = kit.servo[7].angle = val5    #
    M2 = kit.servo[9].angle = val6    #
    M3 = kit.servo[10].angle = val7    #
    M4 = kit.servo[11].angle = val8    # 

while(1):
    if (move == "q"):
        thruster_val(90,90,90,90,90,90,90,90)
        print("Motor's Stopped")
        time.sleep(sleep_sec)
        stop()

    else if (move == "p"):
        thruster_val(90,90,90,90,90,90,90,90)
        print("Motor Moving")
        time.sleep(sleep_sec)
        stop()

cv2.destroyAllWindows()