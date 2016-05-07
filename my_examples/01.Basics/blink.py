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

ledGpio = mraa.Gpio(ledPin)

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

##
# setup: initialization
#
def setup() :
    ledGpio.dir(mraa.DIR_OUT)
##
# loop: what to do "forever"
#
def loop() :
    dot()
    time.sleep(elementGapSecs)
    dash()
    time.sleep(elementGapSecs)
    dash()
    time.sleep(elementGapSecs)
    dot()
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
