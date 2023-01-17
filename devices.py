import gpiozero as gpio
from enum import Enum

class device_manager:    
    def __init__(self):
        self.washing_sensor = gpio.SmoothedInputDevice(27)
        self.drying_sensor = gpio.SmoothedInputDevice(5)
        self.startup_led = gpio.LED(22)

        self.devicelist = {
            DeviceType.WASHING_VIBRATION: self.washing_sensor,
            DeviceType.DRYING_VIBRATION: self.drying_sensor,
            DeviceType.STARTUP_LED: self.startup_led,
        }
        
    def get(self, enu):
        return self.devicelist[enu]
    
    
class DeviceType(Enum):
    WASHING_VIBRATION = 1
    DRYING_VIBRATION = 2
    STARTUP_LED = 3