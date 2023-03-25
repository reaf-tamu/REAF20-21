#!/usr/bin/env python

# Libraries required
from Servo import *
import time
import Servo.py

# Create a new servo object with a reference name
myServo = Servo("First Servo")

# Attaches the servo to pin 3 in Arduino Expansion board
myServo.attach(15)

# Print servo settings
print("")
print("*** Servo Initial Settings ***")
print(myServo)
print("")

try:
    # Sweeps the servo motor forever
    while True:
        # From 0 to 180 degrees
        for angle in range(90,95):
            myServo.write(angle)
            time.sleep(3)

        # From 180 to 0 degrees
        #for angle in range(180,-1,-1):
        #    myServo.write(angle)
        #    time.sleep(3)
            
except KeyboardInterrupt:
	
        print("Sweep ended.")
