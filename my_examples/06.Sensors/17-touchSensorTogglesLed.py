#!/usr/bin/python
#
# 17-touchSensorTogglesLed.py: when the touch sensor is touched, toggle the led
# -----------------------------------------------------------------------------
#
import mraa
import time

LOW = 0
HIGH = 1

digitalInPin = 7
digitalInGpio = mraa.Gpio( digitalInPin )

ledOutPin = 2
ledOutGpio = mraa.Gpio( ledOutPin )
ledOutGpio.dir(mraa.DIR_OUT)

#############################
# Functions
#
def toggleLedState( ledOutState ) :
	print ( 'toggleLedState ledOutState = ' + str(ledOutState) )
	if ( ledOutState == LOW ) :
		 ledOutState = HIGH
	else :
		 ledOutState = LOW
	ledOutGpio.write( ledOutState )
	print ( 'toggleLedState returning ledOutState = ' + str(ledOutState) )
	return ledOutState

#
# mainline loop:
#
ledOutState = LOW
ledOutGpio.write( ledOutState )
loopDelaySecs = 0.1
afterToggleDelaySecs = 3

while True:
	digitalInState = digitalInGpio.read()
	print( 'digitalInState: ' + str(digitalInState) )

	if( digitalInState == 1 ) :
		ledOutState = toggleLedState( ledOutState )
		time.sleep( afterToggleDelaySecs )

	time.sleep( loopDelaySecs )

exit(0)
