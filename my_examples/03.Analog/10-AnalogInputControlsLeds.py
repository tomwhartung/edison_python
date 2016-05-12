#!/usr/bin/python
#
# 10-AnalogInputControlsLeds.py: Use the analog input value on pin A0 to control the brightness of the LED
# --------------------------------------------------------------------------------------------------------
# This example derives from the arduino version, as opposed to the next one,
# 11-AnalogInputControlsLedPwm , which was inspired by the "Make ..." book
#
import mraa
import time

LOW = 0
HIGH = 1

analogInPin = 0
analogInAio = mraa.Aio( analogInPin )

ledOutPin3 = 3
ledOutPin4 = 4
ledOutGpio3 = mraa.Gpio( ledOutPin3 )
ledOutGpio4 = mraa.Gpio( ledOutPin4 )
ledOutGpio3.dir(mraa.DIR_OUT)
ledOutGpio4.dir(mraa.DIR_OUT)

###################################
# Functions for doin the stuffs
#

##
# loop: what to do "forever"
#
def loop() :
	analogInInteger = analogInAio.read()
	analogInFloat = analogInAio.readFloat()
	print( 'analogInInteger: ' + str(analogInInteger) + '; analogInFloat: ' + str(analogInFloat) )
	ledOutGpio3.write(HIGH)
	ledOutGpio4.write(LOW)
	time.sleep( analogInFloat )
	ledOutGpio3.write(LOW)
	ledOutGpio4.write(HIGH)
	time.sleep( analogInFloat )

#
# mainline loop:
#
while True:
	loop()

exit(0)
