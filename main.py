from devices import DeviceType, device_manager
from time import sleep

def startup():
   print("booting up...")
   devices = device_manager()
   washer = devices.get(DeviceType.WASHING_VIBRATION)
   dryer = devices.get(DeviceType.DRYING_VIBRATION)
   
   washer_on = False
   dryer_on = False
   
   washer_count = 0
   dryer_count = 0
   
   print("setup complete!")
   # set up 20ms refresh time to look for values
   while True:
      washer_read = True if washer.value == 0 else False
      dryer_read = True if dryer.value == 0 else False
      
      if washer_read:
         washer_count += 1
         if washer_count > 2000: # 2 seconds of vibration -> might increase
            print("washer has vibrated for two seconds straight")
            # assume it is actually on and activate
            washer_on = True
      else:
         washer_count = 0
         
      if dryer_read:
         dryer_count += 1
         if washer_count > 2000: # 2 seconds of vibration -> might increase
            print("washer has vibrated for two seconds straight")
            # assume it is actually on and activate
            dryer_on = True
      else:
         dryer_count = 0  
      
      # sleeps 20ms
      sleep(.02)
      
   

if __name__ == "__main__":
    startup()