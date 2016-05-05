
import mraa
import time

ledPin = 13
# dotMs  = 200
# dotSecs  = dotMs / 1000
dotSecs  = 0.2
dashSecs = 3 * dotSecs
elementGapSecs = dotSecs
letterGapSecs = dashSecs

x = mraa.Gpio(ledPin)
x.dir(mraa.DIR_OUT)

#
# dot: turn led on for dot milliseconds, then turn it off
#
def dot():
    x.write(1)
    time.sleep(dotSecs)
    x.write(0)
#
# dash: turn led on for dash milliseconds, then turn it off
#
def dash():
    x.write(1)
    time.sleep(dashSecs)
    x.write(0)

#
# mainline loop: write a "P" (for python) in Morse Code "forever"
# A "P" in Morse Code is dot-dash-dash-dot
# Morse Code Reference: https://en.wikipedia.org/wiki/Morse_code#Representation.2C_timing_and_speeds
#
while True:
    dot()
    time.sleep(elementGapSecs)
    dash()
    time.sleep(elementGapSecs)
    dash()
    time.sleep(elementGapSecs)
    dot()
    time.sleep(letterGapSecs)

