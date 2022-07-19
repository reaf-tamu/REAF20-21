import board
import busio
import time
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
shield = adafruit_pca9685.PCA9685(i2c)

shield.frequency = 50

motor_0 = shield.channels[10]

#motor_0.duty_cycle =  40000
while(True):
	angle = int(input("Enter pwm: "))
	motor_0.duty_cycle = angle
	print("i")
#for i in range(0,0xffff,100):
# for i in range(20100,20500,50):
    # motor_0.duty_cycle = i
    # print(i)
    # time.sleep(3)

print("boop")


