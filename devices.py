import gpiozero as gpio
from enum import Enum

class device_manager:    
    def __init__(self):
        self.washing_sensor = gpio.Button(27, bounce_time=.3)
        self.drying_sensor = gpio.Button(5, bounce_time=.3)
        self.startup_led = gpio.LED(22)
        
        # determines how long the sensor should vibrate
        # before registering that it is the washing machine that is on
        self.washing_sensor.hold_time = 5
        self.drying_sensor.hold_time = 5
        
        self.devicelist = {
            DeviceType.WASHING_VIBRATION: self.washing_sensor,
            DeviceType.DRYING_VIBRATION: self.drying_sensor,
            DeviceType.STARTUP_LED: self.startup_led
        }
        
    def get(self, enu):
        return self.devicelist[enu]
    
    
class DeviceType(Enum):
    WASHING_VIBRATION = 1
    DRYING_VIBRATION = 2
    STARTUP_LED = 3