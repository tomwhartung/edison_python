#!/usr/bin/python
#
# 11-AnalogInputControlsLedPwm.py: Use the analog input value to control the brightness of the PWM led
#
import mraa
import time

analogInPin = 0
analogInAio = mraa.Aio( analogInPin )

#
# NOTE: According to our "Make..." book (p.75), the only pins
#    we can use for PWM are digital pins 3, 5, 6, and 9 
#
ledOutPin = 3
ledOutPwm = mraa.Pwm( ledOutPin )
ledOutPwm.enable( True )

##
# loop: what to do "forever"
#
def loop() :
	analogInInteger = analogInAio.read()
	analogInFloat = analogInAio.readFloat()
	print( 'analogInInteger: ' + str(analogInInteger) + '; analogInFloat: ' + str(analogInFloat) )
	ledOutPwm .write( analogInFloat )

#
# mainline: calls loop repeatedly
#
readingGapSecs = 0.5
while True:
	loop()
	time.sleep( readingGapSecs )

exit(0)
