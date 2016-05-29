#!/usr/bin/python
#
# 100-accelerometer.py: working with the accelerometer
# ----------------------------------------------------
#
import mraa
## import time
#
# Init I2C
#
x = mraa.I2c(ledPin)

#
# Set up some addresses and variables for the accelerometer
#
MMA_i2caddr        = 0x1D
MMA8451_REG_WHOAMI = 0x0D
MMA_DEVID          = 0x1A

#
# mainline code: check that we are connected to the MMA8451 chip
#
try :
	x.address( MMA_i2caddr )
	mma_id = x.readReg( MMA8451_REG_WHOAMI )
	if( not mma_id == MMA_DEVID ) :
		print( 'Wrong device found; dev ID = ' + str(mma_id) )
	else :
		print( 'MMA8451 Detected!' )
except :
	print( 'MMA Device NOT Connected!' )

exit(0)
