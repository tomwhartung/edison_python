#!/usr/bin/python
#
# 04-digital-write.py: toggle the leds we are using, each with a different sleep time
# -----------------------------------------------------------------------------------
#
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

led2Secs = 0.25
led3Secs = 0.5
led4Secs = 0.75

##
# setup: initialization
#
def setup() :
	ledGpio2.dir(mraa.DIR_OUT)
	ledGpio3.dir(mraa.DIR_OUT)
	ledGpio4.dir(mraa.DIR_OUT)

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

#
# mainline code: in this case we do not loop, but just turn it off and exit
#
setup()

while( True ) :
	loop()

exit(0)
