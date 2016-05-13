#!/usr/bin/python
#
# 03-digital-read.py: Read and display the digital input value on pin D8 "forever"
# --------------------------------------------------------------------------------
#
import mraa
import time

digitalInPin = 8
digitalInGpio = mraa.Gpio( digitalInPin )

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
