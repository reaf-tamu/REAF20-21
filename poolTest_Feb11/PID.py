from board import SCL, SDA
import busio
import RPi.GPIO as GPIO
import time

from brping import Ping1D
import pinger
import find_global
import datetime



thruster_speed = 0
setpoint = 0.5
oldTime = 0
newTime = 0
timeInterval = 0
error = 0
deerror = 0
accerror = 0
olderror = 0
kp = 5
ki = 1
kd = 0

def pid():
    global oldTime, newTime, error, setpoint, timeInterval, accerror, deerror, olderror, thruster_speed
    c = datetime.datetime.now()
    newTime = c.seconds
    error = -setpoint + pinger.get_distance()
    timeInterval = newTime - oldTime
    accerror+= error*timeInterval
    derror = (error - olderror)/timeInterval
    out = error*kp + (ki*accerror) + (kd*derror)
    print("\n out:")   #The output distance (unit: cm)
    print(error)         #According to the distance
    if out > 5:
        out = 5
    if out < 2:
        out = 2
    thruster_speed = map(out,2,5,-.5,.5) #maps from 2 - 5 meters to -.5(backward) - .5 forwards
    print("\n wheel speed:")  #The output distance (unit: cm)
    print(thruster_speed)         #According to the distance
    olderror = error
    oldTime = newTime
    return int(thruster_speed)

def speedcontrol(speed): #channels 1,3,10,12
    global kit
    kit.continous_servo[1].throttle = speed
    kit.continous_servo[3].throttle = speed
    kit.continous_servo[10].throttle = speed
    kit.continous_servo[12].throttle = speed

if __name__ == 'main':
    speedcontrol(pid())
