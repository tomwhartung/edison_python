#!/usr/bin/python
#
# 09-debouncedButtonTogglesLed.py: when button is pressed, toggle led - debounced version
# ---------------------------------------------------------------------------------------
#
import mraa
import datetime
import time

RELEASED = 0
PRESSED = 1
digitalInPin = 8
digitalInGpio = mraa.Gpio( digitalInPin )
lastInState = RELEASED
currentInState = RELEASED

LOW = 0
HIGH = 1
ledOutPin = 3
ledOutGpio = mraa.Gpio( ledOutPin )
ledOutGpio.dir(mraa.DIR_OUT)
ledOutState = LOW

afterToggleDelaySecs = 0.001
lastDebounceTime = datetime.datetime.today()
debounceWaitMillis = 50     # time to wait for bouncing to end

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
	global lastInState
	global currentInState
	global ledOutState
	global lastDebounceTime
	currentInState = digitalInGpio.read()
	print( 'currentlInState: ' + str(currentInState) )

	currentDatetime = datetime.datetime.today()
	lastDebounceTime = currentDatetime

	if( digitalInState == 1 ) :
		ledOutState = toggleLedState( ledOutState )
		time.sleep( afterToggleDelaySecs )


#
# mainline code: run setup and loop functions
#
setup()
loopDelaySecs = 0.005

while True:
	loop()
	time.sleep( loopDelaySecs )

exit(0)
