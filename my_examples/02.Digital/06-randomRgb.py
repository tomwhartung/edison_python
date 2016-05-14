#!/usr/bin/python
#
# 06-randomRgb.py: toggle the leds we are using, each with a random and different sleep time
# ------------------------------------------------------------------------------------------
#
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

led2Secs = 0
led3Secs = 0
led4Secs = 0
darkSecs = 0

##
# Functions
#
def getRandomSecs() :
	maxSecs = 5.0
	randomSecs = maxSecs * random.random()
	return randomSecs

##
# setup: initialization
#
def setup() :
	ledGpio2.dir(mraa.DIR_OUT)
	ledGpio3.dir(mraa.DIR_OUT)
	ledGpio4.dir(mraa.DIR_OUT)
	print( 'led2Secs: ' + str(led2Secs) )
	print( 'led3Secs: ' + str(led3Secs) )
	print( 'led4Secs: ' + str(led4Secs) )

##
# loop: what to do "forever"
#
def loop() :
	ledGpio2.write( HIGH )
	time.sleep( led2Secs )
	ledGpio2.write( LOW )
	ledGpio3.write( HIGH )
	time.sleep( led3Secs )
	ledGpio3.write( LOW )
	ledGpio4.write( HIGH )
	time.sleep( led4Secs )
	ledGpio4.write( LOW )
	time.sleep( darkSecs )

#
# mainline code: in this case we do not loop, but just turn it off and exit
#
led2Secs = getRandomSecs()
led3Secs = getRandomSecs()
led4Secs = getRandomSecs()
darkSecs = getRandomSecs()

setup()

while( True ) :
	loop()

exit(0)
