import time
import requests
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_ble.advertising.standard import ManufacturerDataField


import adafruit_ble
import adafruit_ble_broadcastnet
from mylight import MyLightClient

ble = adafruit_ble.BLERadio()
print()
print("scanning")
print()
sequence_numbers = {}
checked = []
while True:
    for adv in ble.start_scan(ProvideServicesAdvertisement, timeout=0.5, minimum_rssi=-120):
        
        reversed_address = [adv.address.address_bytes[i] for i in range(5, -1, -1)]
        sensor_address = "{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}".format(*reversed_address)
        print(sensor_address)
        if adv.complete_name == "TestingLight" or MyLightClient in adv.services:
            print("Found: ",sensor_address)
            
        elif sensor_address not in checked:
            print(adv.complete_name,": ",adv.rssi,"dB")
            checked.append(sensor_address)
        else:
            pass
       # print(adv.address.address_bytes)
    #print("nap time")
    time.sleep(5)