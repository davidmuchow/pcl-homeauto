from devices import DeviceType, device_manager
from time import sleep

def startup():
   print("booting up...")

   devices = device_manager()
   washer = devices.get(DeviceType.WASHING_VIBRATION)
   dryer = devices.get(DeviceType.DRYING_VIBRATION)
   
   washer_on = False
   dryer_on = False
   
   def washer_set():
      washer_on = washer.is_held
      print(washer_on)
      
   def dryer_set():
      if dryer_on:
         print("possible end?")
         dryer_on = False
         # Since the dryer was deactivated after it was on, it means it's finished.


      print(dryer_on)
   
   # when held or deactivated set the variables to the correct value
   washer.when_held = washer_set()
   dryer.when_held = dryer_set()
   
   washer.when_deactivated = washer_set()
   dryer.when_deactivated = dryer_set()
   
   

if __name__ == "__main__":
   startup()