import shlex
from devices import DeviceType, device_manager
# import logger
from datetime import datetime
import time
import gpiozero as gpio
from time import sleep
from ifttt_webhook import IftttWebhook
from signal import pause

IFTTT_KEY = "dwNuZAYpSIjYRxBvRYmm0T"

ifttt = IftttWebhook(IFTTT_KEY)

def startup():
   print("booting up...")

   # logger.init()

   devices = device_manager()
   washer = devices.get(DeviceType.WASHING_VIBRATION)
   dryer = devices.get(DeviceType.DRYING_VIBRATION)
   
   led = gpio.LED(22)

   led.on()
   sleep(.05)
   led.off()
   
   global washer_on, washerAtTime, dryer_on, dryerAtTime

   washer_on = False
   washerAtTime = 0
   dryer_on = False
   dryerAtTime = 0
   
   #def washer_set():
   #   global washer_on, washerAtTime
   #   if washer_on:
   #      print("possible end?")
   #      led.on()
   #      washer_on = False
   #      # Since the washer was deactivated after it was on, it means it's finished.
   #      # logger.addWashingMachineEntry(dryerAtTime, time.mktime(datetime.timetuple()))
   #      ifttt.trigger("washer_finished")
   #   else:
   #      washerAtTime = time.time()
   #      led.off()
   #      washer_on = True
      
   #def dryer_set():
   #   global dryer_on, dryerAtTime
   #   if dryer_on:
   #      print("possible end?")
   #      dryer_on = False
   #      # Since the dryer was deactivated after it was on, it means it's finished.
   #      # logger.addDryingMachineEntry(dryerAtTime, time.mktime(datetime.timetuple()))
   #   else:
   #      dryerAtTime = time.time()
   #      dryer_on = True
   
   # when held or deactivated set the variables to the correct value
   #washer.when_held = washer_set
   #dryer.when_held = dryer_set
   
   #washer.when_deactivated = washer_set
   #dryer.when_deactivated = dryer_set

   def sayHello():
      print("yo")

   washer.is_active = sayHello

   pause()

if __name__ == "__main__":
   startup()