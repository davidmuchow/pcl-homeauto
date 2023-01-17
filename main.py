from devices import DeviceType, device_manager
# import logger
from datetime import datetime
import time
from ifttt_webhook import IftttWebhook

IFTTT_KEY = "dwNuZAYpSIjYRxBvRYmm0T"

ifttt = IftttWebhook(IFTTT_KEY)

def startup():
   print("booting up...")

   # logger.init()

   devices = device_manager()
   washer = devices.get(DeviceType.WASHING_VIBRATION)
   dryer = devices.get(DeviceType.DRYING_VIBRATION)
   
   washer_on = False
   washerAtTime = 0
   dryer_on = False
   dryerAtTime = 0
   
   def washer_set(washer_on, washerAtTime):
      if washer_on:
         print("possible end?")
         washer_on = False
         # Since the washer was deactivated after it was on, it means it's finished.
         # logger.addWashingMachineEntry(dryerAtTime, time.mktime(datetime.timetuple()))
         ifttt.trigger("washer_finished")
      else:
         washerAtTime = time.mktime(datetime.timetuple())
         washer_on = True
      
   def dryer_set(dryer_on, dryerAtTime):
      if dryer_on:
         print("possible end?")
         dryer_on = False
         # Since the dryer was deactivated after it was on, it means it's finished.
         # logger.addDryingMachineEntry(dryerAtTime, time.mktime(datetime.timetuple()))
      else:
         dryerAtTime = time.mktime(datetime.timetuple())
         dryer_on = True
   
   # when held or deactivated set the variables to the correct value
   washer.when_held = washer_set(washer_on, washerAtTime)
   dryer.when_held = dryer_set(dryer_on, dryerAtTime)
   
   washer.when_deactivated = washer_set(washer_on, washerAtTime)
   dryer.when_deactivated = dryer_set(dryer_on, dryerAtTime)
   
   

if __name__ == "__main__":
   startup()