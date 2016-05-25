#!/usr/bin/python
#
# 19-debouncedTouchSensorTogglesLed.py: when touch sensor is touched, toggle led - debounced version
# --------------------------------------------------------------------------------------------------
#
import mraa
import datetime
import time

RELEASED = 0
TOUCHED = 1
digitalInPin = 8
digitalInGpio = mraa.Gpio( digitalInPin )
savedTouchSensorState = RELEASED
lastTouchSensorReading = RELEASED

LOW = 0
HIGH = 1
ledOutPin = 3
ledOutGpio = mraa.Gpio( ledOutPin )
ledOutGpio.dir(mraa.DIR_OUT)
ledOutState = HIGH

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
	global savedTouchSensorState
	global lastTouchSensorReading
	global ledOutState
	global lastPressDetectedTime
	currentTouchSensorReading = digitalInGpio.read()

	currentDatetime = datetime.datetime.today()

	if( currentTouchSensorReading != lastTouchSensorReading ) :
		lastPressDetectedTime = currentDatetime

	timeSinceReadingChanged = currentDatetime - lastPressDetectedTime
	#
	# Take the state change seriously only if it persists for debounceWaitSeconds
	#   Save the touch sensor state only if current state is not equal to the saved state
	#     Toggle the led only if the touch sensor state is Pressed
	#
	if( timeSinceReadingChanged.total_seconds() > debounceWaitSeconds ) :
		if( currentTouchSensorReading != savedTouchSensorState ) :
			savedTouchSensorState = currentTouchSensorReading
			if( currentTouchSensorReading == TOUCHED ) :
				ledOutState = toggleLedState( ledOutState )

	ledOutGpio.write( ledOutState )
	lastTouchSensorReading = currentTouchSensorReading

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
