# edison_python

Python versions of the programming examples I am learning about.

## NOTE: We must run these examples as root!!

# Subdirectories

### bluetooth

Contains files found via Chapter 4 of the Make: Getting Started With Intel Edison book by Stephanie Moyerman

* SPP-blink.py - from https://github.com/smoyerman/Edison-Bluetooth-LED
* SPP-loopback.py - from http://downloadmirror.intel.com/24909/eng/SPP-loopback.py (use wget)

See pages 106-112, about using bluetooth to control the LED.

### my_examples

Contains python scripts that demonstrate:

* Digital read and write
* Analog input
* Pulse Width Modulation (PWM)
* I2C (tbd)

These demo programs were inspired by the arduino versions, the node demos, and the book Make: Getting Started With Intel Edison.

For information pertaining to all programs, see the README for the arduino versions:
* edison_arduino repo at https://github.com/tomwhartung/edison_arduino

### run_at_startup

Contains a script to run a python program on startup (if the flag is set), and instructions on how to set that up.
