#!/usr/bin/python
#
# 10-UsingPwmToControlLed.py: Use PWM to control the brightness of a PWM led
#
import mraa
import time

#
# NOTE: the only pins we can use for PWM are digital pins 3, 5, 6, and 9 
#
ledOutPin = 3
ledOutPwm = mraa.Pwm( ledOutPin )
ledOutPwm.enable( True )

##
# loop: what to do "forever"
#
def loop( brightnessPercent ) :
	print( 'brightnessPercent: ' + str(brightnessPercent) )
	brightnessValue = brightnessPercent / 100
	ledOutPwm.write( brightnessPercent )

#
# mainline: calls loop repeatedly
#
loopSleepSecs = 0.5
brightnessPercent = 0
deltaPercent = 5
while True:
	loop( brightnessPercent )
	if( brightnessPercent <= 0 ) :
		deltaPercent = 5
	else if( brightnessPercent >= 100 ) :
		deltaPercent = -5
	brightnessPercent = brightnessPercent + deltaPercent
	time.sleep( loopSleepSecs )

exit(0)
