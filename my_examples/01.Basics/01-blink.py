##
# blinky.py: blink a "P" (for python) in Morse Code "forever"
#
# A "P" in Morse Code is dot-dash-dash-dot
# Morse Code Reference: https://en.wikipedia.org/wiki/Morse_code#Representation.2C_timing_and_speeds
#
import mraa
import time

ledPin = 13
# dotMs  = 200
# dotSecs  = dotMs / 1000
dotSecs  = 0.2
dashSecs = 3 * dotSecs
elementGapSecs = dotSecs
letterGapSecs = dashSecs
wordGapSecs = 7 * dotSecs

ledGpio = mraa.Gpio(ledPin)

###################################
# Primitive Functions (dot and dash)
#
##
# dot: turn led on for dot milliseconds, then turn it off
#
def dot():
    ledGpio.write(1)
    time.sleep(dotSecs)
    ledGpio.write(0)
##
# dash: turn led on for dash milliseconds, then turn it off
#
def dash():
    ledGpio.write(1)
    time.sleep(dashSecs)
    ledGpio.write(0)

###################################
# Functions for each letter
#
# P                   Y                    T      H                 O                N
# dot dash dash dot   dash dot dash dash   dash   dot dot dot dot   dash dash dash   dash dot
#
##
# blink the letter P: dot dash dash dot
#
def blinkLetterP
	dot()
	time.sleep(elementGapSecs)
	dash()
	time.sleep(elementGapSecs)
	dash()
	time.sleep(elementGapSecs)
	dot()
##
# blink the letter Y: dash dot dash dash
#
def blinkLetterY
	dash()
	time.sleep(elementGapSecs)
	dot()
	time.sleep(elementGapSecs)
	dash()
	time.sleep(elementGapSecs)
	dash()
##
# blink the letter T: dot dash dash dot
#
def blinkLetterT: dash
	dash()
##
# blink the letter H: dot dot dot dot
#
def blinkLetterH: dot dot dot dot
	dot()
	time.sleep(elementGapSecs)
	dot()
	time.sleep(elementGapSecs)
	dot()
	time.sleep(elementGapSecs)
	dot()
##
# blink the letter O: dash dash dash
#
def blinkLetterO
	dash()
	time.sleep(elementGapSecs)
	dash()
	time.sleep(elementGapSecs)
	dash()
##
# blink the letter N: dash dot
#
def blinkLetterN
	dash()
	time.sleep(elementGapSecs)
	dot()

###################################
# Setup and loop
#
##
# setup: initialization
#
def setup() :
    ledGpio.dir(mraa.DIR_OUT)
##
# loop: what to do "forever"
#
def loop() :
	blinkLetterP
	time.sleep(letterGapSecs)
	blinkLetterY
	time.sleep(letterGapSecs)
	blinkLetterT
	time.sleep(letterGapSecs)
	blinkLetterH
	time.sleep(letterGapSecs)
	blinkLetterO
	time.sleep(letterGapSecs)
	blinkLetterN
	time.sleep(letterGapSecs)

#
# mainline loop: write a "P" (for python) in Morse Code "forever"
# A "P" in Morse Code is dot-dash-dash-dot
# Morse Code Reference: https://en.wikipedia.org/wiki/Morse_code#Representation.2C_timing_and_speeds
#
setup()

while True:
    loop()

exit(0)
