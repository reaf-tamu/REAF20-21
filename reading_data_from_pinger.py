import time
import csv

from brping import Ping1D
myPing = Ping1D()
myPing.connect_serial("/dev/ttyUSB0", 115200)
if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)
myPing.set_speed_of_sound(1500000,verify = True)

with open('Pinger_data_file1','w',newline = '\n') as file:
    writer = csv.writer(file,delimiter = ',')
    writer.writerow(['Pinger distance'])
    while True:
        data = myPing.get_distance_simple()
        distance_meters = data['distance'] * (10 ** -3)
        writer.writerow([distance_meters])
        time.sleep(1)

