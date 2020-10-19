#!/usr/bin/env python3

import time

from pms5003 import PMS5003, ReadTimeoutError
from bme280 import BME280
import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logging.info("""aerprotek.py - Print readings from the PMS5003 particulate sensor.

Press Ctrl+C to exit!

""")

# BME280 temperature/pressure/humidity sensor
bme280 = BME280()
pms5003 = PMS5003()
time.sleep(1.0)

try:
    print ("human time,min of Day,epoch,temp (C),pressure (hPa),humidity(%),PM1.0 ug/m3,PM2.5 ug/m3,PM10 ug/m3,PM1.0 ug/m3 (atmos), PM2.5 ug/m3 (atmos), PM10 ug/m3 (atmos),>0.3um,>0.5um,>1.0um,>2.5um,>5.0um,>10um")

    while True:
        try:
            n=time.localtime()
            seconds=time.time()
            nice_time=time.ctime(seconds)
            minOfDay=(n.tm_hour * 60) + n.tm_min

            a = pms5003.read()

            temp = bme280.get_temperature()
            pressure = bme280.get_pressure()
            humidity = bme280.get_humidity()

            pm = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(a.data[0],a.data[1],a.data[2],a.data[3],a.data[4],a.data[5],a.data[6],a.data[7],a.data[8],a.data[9],a.data[10],a.data[11])

            output="{0},{1},{2},{3},{4},{5},{6}".format(nice_time, minOfDay, int(seconds),temp,pressure,humidity,pm);
            print(output)          
            time.sleep(10)
        except ReadTimeoutError:
            pms5003 = PMS5003()
except KeyboardInterrupt:
    pass


