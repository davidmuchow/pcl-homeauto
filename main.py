import time
import matplotlib.pyplot as plt
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

plt.ion()
plt.xlabel("time since start")
plt.ylabel("gyro z acceleration")

while True:
	#Read Accelerometer raw value
   acc_x = gyro.read_accel_data(gyro.ACCEL_XOUT_H)
   acc_y = gyro.read_accel_data(gyro.ACCEL_YOUT_H)
   acc_z = gyro.read_accel_data(gyro.ACCEL_ZOUT_H)

   cur_time = int(time.time() - start_time)

   print(cur_time + " " + str(acc_z))   
   plt.plot(cur_time, acc_z)
   plt.show()
   sleep(1)