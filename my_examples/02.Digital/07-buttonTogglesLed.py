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

#############################
# Functions
#
def toggleLedState( ledOutState ) :
	print ( 'toggleLedState ledOutState = ' + str(ledOutState) )
	if ( ledOutState == LOW ) :
		 ledOutState = HIGH
	else :
		 ledOutState = LOW
	print ( 'toggleLedState returning ledOutState = ' + str(ledOutState) )
	return ledOutState

#
# mainline loop:
#
ledOutState = LOW
loopDelaySecs = 0.1

while True:
	ledOutGpio.write( ledOutState )
	digitalInState = digitalInGpio.read()
	print( 'digitalInState: ' + str(digitalInState) )
	if( digitalInState == 1 ) :
		ledOutState = toggleLedState( ledOutState )

	time.sleep( loopDelaySecs )

exit(0)
