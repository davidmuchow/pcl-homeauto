import gpiozero as gpio
from enum import Enum

class device_manager:    
    def __init__(self):
        self.washing_sensor = gpio.MotionSensor(27)
        self.drying_sensor = gpio.MotionSensor(5)

        self.devicelist = {
            DeviceType.WASHING_VIBRATION: self.washing_sensor,
            DeviceType.DRYING_VIBRATION: self.drying_sensor,
        }
        
    def get(self, enu):
        return self.devicelist[enu]
    
    
class DeviceType(Enum):
    WASHING_VIBRATION = 1
    DRYING_VIBRATION = 2