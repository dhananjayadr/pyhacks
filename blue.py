import time
from adafruit_ble import BLERadio


ble = BLERadio()
for advertisement in ble.start_scan():
    addr = advertisement.address
    if str(addr).split('"')[-2] == '<BLE-UUID>':
        device = ble.connect(addr, timeout=120)
        time.sleep(5)
        device.disconnect()
        break
ble.stop_scan()
