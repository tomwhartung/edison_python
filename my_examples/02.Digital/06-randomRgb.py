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

aed2State = HIGH
led3State = HIGH
led4State = HIGH

maxCycleSecs = 5.0
led2CycleSecs = 0
led3CycleSecs = 0
led4CycleSecs = 0

##
# Functions
#
def getRandomCycleSecs() :
	randomCycleSecs = maxCycleSecs * random.random()
	return randomCycleSecs

##
# Determine whether it is time to change the state of an led
#
def isTimeToToggle( cycleStartDatetime, cycleSecs ) :
	cycleStartSecsOnly = getAttr( cycleStartDatetime, 'second' )
	cycleStartMicrosecs = getAttr( cycleStartDatetime, 'microsecond' )
	cycleStartSecs = cycleStartSecsOnly + ( cycleStartMicrosecs / 1000000 )
	currentDatetime = datetime.today()
	currentSecsOnly = getAttr( currentDatetime, 'second' )
	currentMicrosecs = getAttr( currentDatetime, 'microsecond' )
	currentSecs = currentSecsOnly + ( currentMicrosecs / 1000000 )
	elapsedSecs = currentSecs - cycleStartSecs
	print( 'currentSecs - cycleStartSecs = ' + str(currentSecs) + ' - ' + str(cycleStartSecs) + ' = ' + elapsedSecs )
	if ( cycleSecs < elapsedSecs ) :
		return True
	else :
		return False

##
# Return the opposite of the state passed in
# This may seem unnecessary, but I just do not like statements of the form "state = !state"
#
def toggleState( currentState )
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
	print( 'led2CycleSecs: ' + str(led2CycleSecs) )
	print( 'led3CycleSecs: ' + str(led3CycleSecs) )
	print( 'led4CycleSecs: ' + str(led4CycleSecs) )

##
# loop: what to do "forever"
#
def loop() :
	if ( isTimeToToggle( led2Datetime, led2CycleSecs )  ):
		led2State = toggleState( led2State )
		ledGpio2.write( led2State )
	if ( isTimeToToggle( )  ):
		led3State = toggleState( led3State )
		ledGpio3.write( led3State )
	if ( isTimeToToggle( )  ):
		led4State = toggleState( led4State )
		ledGpio4.write( led4State )

#
# mainline code: in this case we do not loop, but just turn it off and exit
#
led2CycleSecs = getRandomCycleSecs()
led3CycleSecs = getRandomCycleSecs()
led4CycleSecs = getRandomCycleSecs()

led2Datetime = datetime.today()
led3Datetime = datetime.today()
led4Datetime = datetime.today()

ledGpio2.write( led2State )
ledGpio3.write( led3State )
ledGpio4.write( led4State )

setup()

while( True ) :
	loop()

exit(0)
