#!/usr/bin/python
#
# 06-randomRgb.py: toggle the leds we are using, each with a random and different sleep time
# ------------------------------------------------------------------------------------------
#
from datetime import *
import math, random
import mraa
import time

LOW = 0
HIGH = 1

ledPin2 = 2
ledPin3 = 3
ledPin4 = 4

ledGpio2 = mraa.Gpio( ledPin2 )
ledGpio3 = mraa.Gpio( ledPin3 )
ledGpio4 = mraa.Gpio( ledPin4 )

led2State = HIGH
led3State = HIGH
led4State = HIGH

maxCycleSecs = 1.0
led2CycleMicrosecs = 0
led3CycleMicrosecs = 0
led4CycleMicrosecs = 0

##
# Functions
#
def getRandomCycleMicrosecs() :
	randomCycleMicrosecs = maxCycleSecs * random.random()
	return randomCycleMicrosecs

##
# Determine whether it is time to change the state of an led
#
def isTimeToToggle( cycleStartDatetime, cycleSecs ) :
	cycleStartSecsOnly = cycleStartDatetime.second
	cycleStartMicrosecsOnly = cycleStartDatetime.microsecond
	cycleStartTotalMicrosecs = (1000000 * cycleStartSecsOnly) + cycleStartMicrosecsOnly
	currentDatetime = datetime.today()
	currentSecsOnly = currentDatetime.second
	currentMicrosecsOnly = currentDatetime.microsecond
	currentTotalMicrosecs = (1000000 * currentSecsOnly) + currentMicrosecsOnly
	elapsedMicrosecs = currentTotalMicrosecs - cycleStartTotalMicrosecs
	## print( 'currentTotalMicrosecs - cycleStartTotalMicrosecs = ' + str(currentTotalMicrosecs) + ' - ' + str(cycleStartTotalMicrosecs) + ' = ' + str(elapsedMicrosecs) )
	if ( cycleSecs < elapsedMicrosecs ) :
		return True
	else :
		return False

##
# Return the opposite of the state passed in
# This may seem unnecessary, but I just do not like statements of the form "state = !state"
#
def toggleState( currentState ) :
	if ( currentState == HIGH ) :
		return LOW
	else :
		return HIGH

##
# setup: initialization
#
def setup() :
	ledGpio2.dir(mraa.DIR_OUT)
	ledGpio3.dir(mraa.DIR_OUT)
	ledGpio4.dir(mraa.DIR_OUT)
	print( 'led2CycleMicrosecs: ' + str(led2CycleMicrosecs) )
	print( 'led3CycleMicrosecs: ' + str(led3CycleMicrosecs) )
	print( 'led4CycleMicrosecs: ' + str(led4CycleMicrosecs) )

##
# loop: what to do "forever"
#
def loop() :
	global led2State
	global led3State
	global led4State
	if ( isTimeToToggle( led2Datetime, led2CycleMicrosecs )  ):
		led2State = toggleState( led2State )
		ledGpio2.write( led2State )
	if ( isTimeToToggle( led3Datetime, led3CycleMicrosecs )  ):
		led3State = toggleState( led3State )
		ledGpio3.write( led3State )
	if ( isTimeToToggle( led4Datetime, led4CycleMicrosecs )  ):
		led4State = toggleState( led4State )
		ledGpio4.write( led4State )

#
# mainline code: in this case we do not loop, but just turn it off and exit
#
led2CycleMicrosecs = getRandomCycleMicrosecs()
led3CycleMicrosecs = getRandomCycleMicrosecs()
led4CycleMicrosecs = getRandomCycleMicrosecs()

led2Datetime = datetime.today()
led3Datetime = datetime.today()
led4Datetime = datetime.today()

displayLedDatetime( '2', led2Datetime )
displayLedDatetime( '3', led3Datetime )
displayLedDatetime( '4', led4Datetime )
##
# debug function to help us convert from using floats to using integers for the timing variables
#
def displayLedDatetime( ledNo, ledDatetime ) :
	ledSecsOnly = ledDatetime.second
	ledMicrosecsOnly = ledDatetime.microsecond
	ledTotalMicrosecs = (1000000 * ledSecsOnly ) + ledMicrosecsOnly
	print( 'ledNo: ' + ledNo + ': ledSecsOnly + ledMicrosecsOnly = ' + str(ledSecsOnly) + ' + ' + str(ledMicrosecsOnly) + ' = ledMicrosecs = ' + str(ledMicrosecs) )

ledGpio2.write( led2State )
ledGpio3.write( led3State )
ledGpio4.write( led4State )

setup()

while( True ) :
	loop()

exit(0)
