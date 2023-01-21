import smbus2

class gyroscope:
    def __init__(self):
        #some MPU6050 Registers and their Address
        self.PWR_MGMT_1 = 0x6B
        self.SMPLRT_DIV = 0x19
        self.CONFIG = 0x1A
        self.GYRO_CONFIG = 0x1B
        self.INT_ENABLE = 0x38
        self.ACCEL_XOUT_H = 0x3B
        self.ACCEL_YOUT_H = 0x3D
        self.ACCEL_ZOUT_H = 0x3F

        self.bus = smbus2.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
        self.Device_Address = 0x68   # MPU6050 device address
        # write to sample rate register
        self.bus.write_byte_data(self.Device_Address, self.SMPLRT_DIV, 7)
        
        # write to power management register
        self.bus.write_byte_data(self.Device_Address, self.PWR_MGMT_1, 1)
        
        # write to Configuration register
        self.bus.write_byte_data(self.Device_Address, self.CONFIG, 0)
        
        # write to Gyro configuration register
        self.bus.write_byte_data(self.Device_Address, self.GYRO_CONFIG, 24)
        
        # write to interrupt enable register
        self.bus.write_byte_data(self.Device_Address, self.INT_ENABLE, 1)

    def read_raw_data(self, addr):
	    # accelero and Gyro value are 16-bit
        high = self.bus.read_byte_data(self.Device_Address, addr)
        low = self.bus.read_byte_data(self.Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value
    
    def read_accel_data(self, addr):
        return self.read_raw_data(addr) / 16384.0
