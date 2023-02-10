# from brping import Ping1D
# myPing = Ping1D()
# myPing.connect_serial("COM3", 115200)
# if myPing.initialize() is False:
#     print("Failed to initialize Ping!")
#     exit(1)
from brping import Ping1D
myPing = Ping1D()
myPing.connect_serial("COM3", 115200)
if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)
    
def get_distance():
    myPing.set_speed_of_sound(1500000,verify = True)
    data = myPing.get_distance_simple()
    distance_meters= data['distance']*(10**-3)
    return distance_meters
    # if data:
    #     print("Distance: %s\tConfidence: %s%%" % (distance_meters, data["confidence"]))
    # else:
    #     print("Failed to get distance data")
    # elif letter == 'pcb temp':
    #     data = myPing.get_pcb_temperature()
    #     if data:
    #         print(f'The pcb temperature is {data["pcb_temperature"]/100} celcius')
    #     else:
    #         print("Failed to get pcb temperature data")
    # elif letter == 'processor temp':
    #     data = myPing.get_processor_temperature()
    #     if data:
    #         print(f'The processor temperature is {data["processor_temperature"]/100} celcius')
    #     else:
    #         print("Failed to get processor temperature data")
    # elif letter == 'range':
    #     data = myPing.get_range()
    #     if data:
    #         print(f'The range is {data} mm')
    #     else:
    #         print("Failed to get range data")
    # else:
    #     continue
