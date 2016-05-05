#!/bin/sh
#
# To run the script referenced below at startup:
# (1) copy this script (automatic.sh) into /etc/init.d (as root)
# (2) run this command (as root):
#     update-rc.d automatic.sh 
#
if [ -f ~/iot/flags/run_python_on_startup.flag ]; then
	python /home/root/iot/customizations/edison_python/my_examples/01.Basics/blink.py
fi

