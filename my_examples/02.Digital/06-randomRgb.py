#!/usr/bin/python
#
# 06-randomRgb.py: toggle the leds we are using, each with a random and different sleep time
# ------------------------------------------------------------------------------------------
#
from datetime import *
import math, random
import mraa
import time
import sys

LOW = 0
HIGH = 1

ledPin2 = 2
ledPin3 = 3
ledPin4 = 4

maxCycleSecs = 3.0
led2CycleMicrosecs = 0
led3CycleMicrosecs = 0
led4CycleMicrosecs = 0

led2LastDatetime = 0
led3LastDatetime = 0
led4LastDatetime = 0

##
# Functions
#
def getRandomCycleMicrosecs() :
	randomCycleMicrosecs = 1000000 * ( maxCycleSecs * random.random() )
	return int(randomCycleMicrosecs)

##
# Determine whether it is time to change the state of an led
# Try using timedelta
#
def isTimeToToggle( cycleStartDatetime, cycleMicrosecs ) :
	currentDatetime = datetime.today()
	elapsedTimedelta = currentDatetime - cycleStartDatetime
	elapsedMicrosecs = elapsedTimedelta.total_seconds() * 1000000
	if ( cycleMicrosecs < elapsedMicrosecs ) :
		print( 'cycleMicrosecs: ' + str(cycleMicrosecs) + '; elapsedMicrosecs: ' + str(elapsedMicrosecs) )
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
# debug function to help us convert from using floats to using integers for the timing variables
#
def displayLastDatetime( ledNo, ledLastDatetime ) :
	ledSecsOnly = ledLastDatetime.second
	ledMicrosecsOnly = ledLastDatetime.microsecond
	ledTotalMicrosecs = (1000000 * ledSecsOnly ) + ledMicrosecsOnly
	print( 'led' + ledNo + 'LastDateTime: ' + str(ledSecsOnly * 1000000) + ' + ' + str(ledMicrosecsOnly) + ' = ' + str(ledTotalMicrosecs) )

##
# setup: initialization
#
def setup() :
	global led2State, ledGpio2
	global led3State, ledGpio3
	global led4State, ledGpio4
	global led2LastDatetime, led2CycleMicrosecs
	global led3LastDatetime, led3CycleMicrosecs
	global led4LastDatetime, led4CycleMicrosecs
	led2State = HIGH
	led3State = HIGH
	led4State = HIGH
	ledGpio2 = mraa.Gpio( ledPin2 )
	ledGpio3 = mraa.Gpio( ledPin3 )
	ledGpio4 = mraa.Gpio( ledPin4 )
	ledGpio2.dir(mraa.DIR_OUT)
	ledGpio3.dir(mraa.DIR_OUT)
	ledGpio4.dir(mraa.DIR_OUT)
	ledGpio2.write( led2State )
	ledGpio3.write( led3State )
	ledGpio4.write( led4State )
	led2LastDatetime = datetime.today()
	led3LastDatetime = datetime.today()
	led4LastDatetime = datetime.today()
	led2CycleMicrosecs = getRandomCycleMicrosecs()
	led3CycleMicrosecs = getRandomCycleMicrosecs()
	led4CycleMicrosecs = getRandomCycleMicrosecs()
	print( '( ledSecsOnly * 1000000 ) + ledMicrosecsOnly = ledTotalMicrosecs' )
	displayLastDatetime( '2', led2LastDatetime )
	displayLastDatetime( '3', led3LastDatetime )
	displayLastDatetime( '4', led4LastDatetime )
	print( 'led2CycleMicrosecs: ' + str(led2CycleMicrosecs) )
	print( 'led3CycleMicrosecs: ' + str(led3CycleMicrosecs) )
	print( 'led4CycleMicrosecs: ' + str(led4CycleMicrosecs) )


##
# loop: what to do "forever"
#
def loop( counter ) :
	global led2State, led2LastDatetime
	global led3State, led3LastDatetime
	global led4State, led4LastDatetime
	if ( isTimeToToggle( led2LastDatetime, led2CycleMicrosecs )  ) :
		led2State = toggleState( led2State )
		ledGpio2.write( led2State )
		led2LastDatetime = datetime.today()
		onOrOff = 'ON' if led2State else 'off'
		sys.stdout.write( 'T2-' + onOrOff + '-' + str(counter) + ' ' )
	if ( isTimeToToggle( led3LastDatetime, led3CycleMicrosecs )  ) :
		led3State = toggleState( led3State )
		ledGpio3.write( led3State )
		led3LastDatetime = datetime.today()
		## onOrOff = 'ON' if led3State else 'off'
		## sys.stdout.write( 'T3-' + onOrOff + ' ' )
	if ( isTimeToToggle( led4LastDatetime, led4CycleMicrosecs )  ) :
		led4State = toggleState( led4State )
		ledGpio4.write( led4State )
		led4LastDatetime = datetime.today()
		## onOrOff = 'ON' if led4State else 'off'
		## sys.stdout.write( 'T4-' + onOrOff + ' ' )
	loopSleepSecs = 0.1
	time.sleep( loopSleepSecs )
	## sys.stdout.write( str(counter) + ' ' )
	sys.stdout.flush()

#
# mainline code: call setup and loop
#
setup()

counter = 0
while( True ) :
	loop( counter )
	counter += 1

exit(0)
