#!/usr/bin/python
import ms5837
import time

#sensor = ms5837.MS5837_30BA() # Default I2C bus is 1 (Raspberry Pi 3)
#sensor = ms5837.MS5837_30BA(0) # Specify I2C bus
sensor = ms5837.MS5837_02BA()
#sensor = ms5837.MS5837_02BA(0)
#sensor = ms5837.MS5837(model=ms5837.MS5837_MODEL_30BA, bus=0) # Specify model and bus

# We must initialize the sensor before reading it
if not sensor.init():
        print("Sensor could not be initialized")
        exit(1)

# We have to read values from sensor to update pressure and temperature
if not sensor.read():
    print("Sensor read failed!")
    exit(1)


pressure = sensor.pressure(ms5837.UNITS_psi)


temp = sensor.temperature(ms5837.UNITS_Centigrade)


freshwaterDepth = sensor.depth() # default is freshwater
sensor.setFluidDensity(ms5837.DENSITY_SALTWATER)
saltwaterDepth = sensor.depth() # No nead to read() again
sensor.setFluidDensity(1000) # kg/m^3


def ps_data(pressure,temp,freshwaterDepth,saltwaterDepth): # x is whatever the pressure sensors outputs
    import csv
    header = ['pressure','temp','freshwaterDepth','saltwaterDepth']
    append = [pressure,temp,freshwaterDepth,saltwaterDepth]
    with open('pressure_sensor_data.csv','a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(header)
        while True:
            writer.writerow(append)
            time.sleep(1)
    csvFile.close()
 
ps_data(pressure,temp,freshwaterDepth,saltwaterDepth)


#print(pressure)
#print(temp)
#print(freshwaterDepth)
#print(saltwaterDepth)

#time.sleep(5)

# Spew readings






    