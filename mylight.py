from adafruit_ble.services import Service
from adafruit_ble.uuid import VendorUUID
from adafruit_ble.characteristics import Characteristic
from adafruit_ble.characteristics.int import Uint8Characteristic

class MyLightClient(Service):
    uuid = VendorUUID("6BFD8F3F-A704-4111-8DCE-F571BA26B40B")
    _control = Characteristic(
        uuid = VendorUUID("6BFD8F3E-A704-4111-8DCE-F571BA26B40B"),
        max_length=7
    )
    _light_level= Uint8Characteristic(
        uuid = VendorUUID("6BFD8F3D-A704-4111-8DCE-F571BA26B40B"),
        initial_value=100,
        properties=( Characteristic.READ | Characteristic.WRITE |  Characteristic.WRITE_NO_RESPONSE)
    )
    print("my light init")

