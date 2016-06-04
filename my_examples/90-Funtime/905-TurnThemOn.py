#!/usr/bin/python
#
# 905-turnThemOn.py: turn on all the leds we are using, for a cool photo
# ----------------------------------------------------------------------
#
import mraa
import time

LOW = 0
HIGH = 1

ledPin13 = 13   # the onboard led
ledPin2 = 2
ledPin3 = 3
ledPin4 = 4

ledGpio13 = mraa.Gpio( ledPin13 )
ledGpio2 = mraa.Gpio( ledPin2 )
ledGpio3 = mraa.Gpio( ledPin3 )
ledGpio4 = mraa.Gpio( ledPin4 )

##
# setup: initialization
#
def setup() :
    ledGpio13.dir(mraa.DIR_OUT)
    ledGpio2.dir(mraa.DIR_OUT)
    ledGpio3.dir(mraa.DIR_OUT)
    ledGpio4.dir(mraa.DIR_OUT)

##
# loop: what to do "forever"
#
def loop() :
    ledGpio13.write( HIGH )
    ledGpio2.write( HIGH )
    ledGpio3.write( HIGH )
    ledGpio4.write( HIGH )

#
# mainline code: in this case we do not loop, but just turn it off and exit
#
setup()

loop()

exit(0)
