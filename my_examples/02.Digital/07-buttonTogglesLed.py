#!/usr/bin/python
#
# 07-buttonTogglesLed.py: when the button is pressed, toggle the led
# ------------------------------------------------------------------
#
import mraa
import time

LOW = 0
HIGH = 1

digitalInPin = 8
digitalInGpio = mraa.Gpio( digitalInPin )

ledOutPin = 3
ledOutGpio = mraa.Gpio( ledOutPin )
ledOutGpio.dir(mraa.DIR_OUT)

###################################
# Functions for doin the stuffs
#

##
# loop: what to do "forever"
#
def loop() :
	digitalInInteger = digitalInGpio.read()
	print( 'digitalInInteger: ' + str(digitalInInteger) )
	if( digitalInInteger == 1 ) :
		ledGpio3.write( HIGH )
	else :
		ledGpio3.write( LOW )

#
# mainline loop:
#
sleepSecs = 0.5
while True:
	loop()
	time.sleep( sleepSecs )

exit(0)
