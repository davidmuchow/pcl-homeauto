import time
# import logger
from datetime import datetime
import gpiozero as gpio
from time import sleep
from ifttt_webhook import IftttWebhook
from signal import pause

from gyroscope import gyroscope

IFTTT_KEY = "dwNuZAYpSIjYRxBvRYmm0T"

ifttt = IftttWebhook(IFTTT_KEY)

start_time = int(time.time())

print("Reading Data of Gyroscope and Accelerometer")

activated = False
led = gpio.LED(5)
gyro = gyroscope()

while True:
	
	#Read Accelerometer raw value
   acc_x = gyro.read_accel_data(gyro.ACCEL_XOUT_H)
   acc_y = gyro.read_accel_data(gyro.ACCEL_YOUT_H)
   acc_z = gyro.read_accel_data(gyro.ACCEL_ZOUT_H)

   print(int(time.time() - start_time))

   if abs(Az) - .05 > 0 and not activated:
      activated = True
      led.on()
      print("machine activate")

   if not activated:
      led.off()
   
   sleep(3)