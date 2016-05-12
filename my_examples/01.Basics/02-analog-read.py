#!/usr/bin/python
#
# 02-analog-read.py: Read and display the analog input value on pin A0 "forever"
#
import mraa
import time

analogInPin = 0
analogInAio = mraa.Aio( analogInPin )

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
	analogInInteger = analogInAio.read()
	analogInFloat = analogInAio.readFloat()
	print( 'analogInInteger: ' + str(analogInInteger) + '; analogInFloat: ' + str(analogInFloat) )
	time.sleep( readingGapSecs )

#
# mainline loop:
#
while True:
    loop()

exit(0)
