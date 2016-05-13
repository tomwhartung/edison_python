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

ledOutState = LOW

#############################
# Functions
#
def toggleLedState( ledOutState ) :
	if ( ledOutState == LOW ) :
		 ledOutState = HIGH
	else :
		 ledOutState = LOW
	return ledOutState

##
# loop: what to do "forever"
#
def loop() :
	ledOutGpio.write( ledOutState )
	digitalInState = digitalInGpio.read()
	print( 'digitalInState: ' + str(digitalInState) )
	if( digitalInInteger == 1 ) :
		ledOutState = toggleLedState( ledOutState )

#
# mainline loop:
#
loopDelaySecs = 0.1
while True:
	loop()
	time.sleep( loopDelaySecs )

exit(0)
