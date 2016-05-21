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
	brightnessValue = float( brightnessPercent ) / 100
	print( 'brightnessPercent: ' + str(brightnessPercent) + '; brightnessValue: ' + str(brightnessValue) )
	ledOutPwm.write( brightnessValue )

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
	elif( brightnessPercent >= 100 ) :
		deltaPercent = -5
	brightnessPercent = brightnessPercent + deltaPercent
	time.sleep( loopSleepSecs )

exit(0)
