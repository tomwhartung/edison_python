#!/usr/bin/python
#
# 03-digital-read.py: Read and display the digital input value on pin D6 "forever"
# --------------------------------------------------------------------------------
#
import mraa
import time

digitalInPin = 0
digitalInGpio = mraa.Gpio( digitalInPin )

## ledOutPin = 3
## ledOutGpio = mraa.Gpio( ledOutPin )
## ledOutGpio.dir(mraa.DIR_OUT)

###################################
# Functions for doin the stuffs
#

##
# loop: what to do "forever"
#
def loop() :
	readingGapSecs = 0.5
	digitalInInteger = digitalInGpio.read()
	print( 'digitalInInteger: ' + str(digitalInInteger) )
	time.sleep( readingGapSecs )

#
# mainline loop:
#
while True:
    loop()

exit(0)
