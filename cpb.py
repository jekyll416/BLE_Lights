"""
Circuit Playground Bluefruit Ornament Proximity
This demo uses advertising to set the color of scanning devices depending on the strongest broadcast
signal received. Circuit Playgrounds can be switched between advertising and scanning using the
slide switch. The buttons change the color when advertising.
"""

import time
from adafruit_circuitplayground.bluefruit import cpb

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from mylight import MyLightClient
# The color pickers will cycle through this list with buttons A and B.
color_options = [0x110000,
                 0x111100,
                 0x001100,
                 0x001111,
                 0x000011,
                 0x110011,
                 0x111111,
                 0x221111,
                 0x112211,
                 0x111122]
i = 0
current_value=0
ble = BLERadio()
print("ble loaded")
light = MyLightClient()
print("mylight client init")

advertisement = ProvideServicesAdvertisement(light)
ble._adapter.name = "TestingLight"


def waitforconnect():
    print("Advertising.")
    central = False
    ble.start_advertising(advertisement)

    print("Waiting.")
    while not ble.connected:
        pass


    # We're now connected, one way or the other
    print("Stopping advertising.")
    ble.stop_advertising()
    for connection in ble.connections:
        return connection


while True:
    central = waitforconnect()
    print("Connected")
    while ble.connected:
        percent = round(light._light_level/256*10)
        if percent != current_value:
            cpb.pixels.fill(0x000000)
            for i in range(0, percent):
                cpb.pixels[i] = color_options[i]
            cpb.pixels.show()
            current_value=percent
        time.sleep(1)
    print("Disconnected")
    print()

