import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
global washer_on
washer_on = False

global last_time_on
last_time_on = time.time()


def animate(i, xs, ys):
   # Read temperature (Celsius) from TMP102
   temp_c = max(abs(round(gyro.read_accel_data(gyro.ACCEL_ZOUT_H), 2)) - .035, 0)

   if temp_c > .03:
      washer_on = True
      last_time_on = time.time()

   if (time.time() - last_time_on) > 15:
      print("off")
      ifttt.trigger("washer_finished")

   # Add x and y to lists
   xs.append(datetime.now().strftime('%H:%M:%S.%f'))
   ys.append(temp_c)

    # Limit x and y lists to 20 items
   xs = xs[-20:]
   ys = ys[-20:]

    # Draw x and y lists
   ax.clear()
   ax.plot(xs, ys)

   # Format plot
   plt.xticks(rotation=45, ha='right')
   plt.subplots_adjust(bottom=0.30)
   plt.title('Z Gyro')
   plt.ylabel('Acceleration in G')


ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()

# while True:
# 	#Read Accelerometer raw value
#    acc_x = gyro.read_accel_data(gyro.ACCEL_XOUT_H)
#    acc_y = gyro.read_accel_data(gyro.ACCEL_YOUT_H)
#    acc_z = gyro.read_accel_data(gyro.ACCEL_ZOUT_H)

#    cur_time = int(time.time() - start_time)

#    print(str(cur_time) + " " + str(acc_z))   
#    plt.plot(cur_time, acc_z)
#    sleep(1)