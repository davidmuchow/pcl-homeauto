from devices import DeviceType, device_manager
import time
# import logger
from datetime import datetime
import smbus2
import gpiozero as gpio
from time import sleep
from ifttt_webhook import IftttWebhook
from signal import pause

IFTTT_KEY = "dwNuZAYpSIjYRxBvRYmm0T"

ifttt = IftttWebhook(IFTTT_KEY)

start_time = int(time.time())

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47


def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	
	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)
	
	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	
	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus2.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")

activated = False

while True:
	
	#Read Accelerometer raw value
   acc_x = read_raw_data(ACCEL_XOUT_H)
   acc_y = read_raw_data(ACCEL_YOUT_H)
   acc_z = read_raw_data(ACCEL_ZOUT_H)

   #Read Gyroscope raw value
   gyro_x = read_raw_data(GYRO_XOUT_H)
   gyro_y = read_raw_data(GYRO_YOUT_H)
   gyro_z = read_raw_data(GYRO_ZOUT_H)
	
   #Full scale range +/- 250 degree/C as per sensitivity scale factor
   Ax = acc_x/16384.0
   Ay = acc_y/16384.0
   Az = acc_z/16384.0

   Gx = gyro_x/131.0
   Gy = gyro_y/131.0
   Gz = gyro_z/131.0

   print(int(time.time() - start_time))
   print("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az)

   if abs(Az) - .4 > 0 and not activated:
      activated = True
      print("machine activate")
   
   sleep(10)

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