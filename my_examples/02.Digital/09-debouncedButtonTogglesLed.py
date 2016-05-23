#!/usr/bin/python
#
# 09-debouncedButtonTogglesLed.py: when button is pressed, toggle led - debounced version
# ---------------------------------------------------------------------------------------
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
##
# Initialize the LED as output and set its initial state
#
def setup() :
	ledOutGpio.dir(mraa.DIR_OUT)
	ledOutGpio.write( ledOutState )

##
# Toggles the state of the led
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

##
# Loop: runs "forever" (until program stopped)
#
def loop() :
	global ledOutState
	digitalInState = digitalInGpio.read()
	print( 'digitalInState: ' + str(digitalInState) )

	if( digitalInState == 1 ) :
		ledOutState = toggleLedState( ledOutState )
		time.sleep( afterToggleDelaySecs )


#
# mainline code: run setup and loop functions
#
setup()
loopDelaySecs = 0.1

while True:
	loop()
	time.sleep( loopDelaySecs )

exit(0)
