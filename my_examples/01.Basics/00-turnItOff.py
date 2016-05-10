##
# turnItOff.py: turn off the led, no sense wearing it out
#
import mraa
import time

ledPin = 13
ledGpio = mraa.Gpio(ledPin)

##
# setup: initialization
#
def setup() :
    ledGpio.dir(mraa.DIR_OUT)
##
# loop: what to do "forever"
#
def loop() :
    ledGpio.write(0)


#
# mainline code: in this case we do not loop, but just turn it off and exit
#
setup()

loop()

exit(0)
