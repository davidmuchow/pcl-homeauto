from devices import DeviceType, device_manager
from time import sleep

def startup():
   print("booting up...")
   devices = device_manager()
   washer = devices.get(DeviceType.WASHING_VIBRATION)
   
   print("setup complete!")
   
   

if __name__ == "__main__":
    startup()