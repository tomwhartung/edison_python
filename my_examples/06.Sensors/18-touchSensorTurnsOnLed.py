#!/usr/bin/python
#
# 08-buttonTurnsOnLed.py: when the button is pressed, turn on the led
# -------------------------------------------------------------------
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

##
# loop: what to do "forever"
#
def loop() :
	digitalInInteger = digitalInGpio.read()
	print( 'digitalInInteger: ' + str(digitalInInteger) )
	if( digitalInInteger == 1 ) :
		ledOutGpio.write( HIGH )
	else :
		ledOutGpio.write( LOW )

#
# mainline loop:
#
sleepSecs = 0.5
while True:
	loop()
	time.sleep( sleepSecs )

exit(0)
