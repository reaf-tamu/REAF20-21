import serial

ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)

while(1):
	print(ser.readline())

