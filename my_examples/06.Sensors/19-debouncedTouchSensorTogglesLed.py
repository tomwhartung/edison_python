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
savedButtonState = RELEASED
lastButtonReading = RELEASED

LOW = 0
HIGH = 1
ledOutPin = 3
ledOutGpio = mraa.Gpio( ledOutPin )
ledOutGpio.dir(mraa.DIR_OUT)
ledOutState = LOW

## afterToggleDelaySecs = 0.001
lastPressDetectedTime = datetime.datetime.today()
debounceWaitSeconds = 0.05     # seconds to wait for bouncing to end

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
	print ( 'toggleLedState returning ledOutState = ' + str(ledOutState) )
	return ledOutState

##
# Loop: runs "forever" (until program stopped)
#
def loop() :
	global savedButtonState
	global lastButtonReading
	global ledOutState
	global lastPressDetectedTime
	currentButtonReading = digitalInGpio.read()

	currentDatetime = datetime.datetime.today()

	if( currentButtonReading != lastButtonReading ) :
		lastPressDetectedTime = currentDatetime

	timeSinceReadingChanged = currentDatetime - lastPressDetectedTime
	#
	# Take the change seriously only if the change persists for debounceWaitSeconds
	#   Save the button state only if current state is not equal to the saved state
	#     Toggle the led only if the button state is Pressed
	#
	if( timeSinceReadingChanged.total_seconds() > debounceWaitSeconds ) :
		if( currentButtonReading != savedButtonState ) :
			savedButtonState = currentButtonReading
			if( currentButtonReading == PRESSED ) :
				ledOutState = toggleLedState( ledOutState )

	ledOutGpio.write( ledOutState )
	lastButtonReading = currentButtonReading

#
# mainline code: run setup and loop functions
#
setup()
loopDelaySecs = 0.005
currentDatetime = datetime.datetime.today()
lastPressDetectedTime = currentDatetime

while True :
	loop()
	time.sleep( loopDelaySecs )

exit(0)
