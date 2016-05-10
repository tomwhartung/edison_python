#!/bin/sh
#
# Note: this file is kept in the edison_python repo, run_at_startup directory
#
# To run this script at startup:
# (1) copy this script (automatic.sh) into /etc/init.d (as root)
# (2) run this command (as root):
#     update-rc.d automatic.sh defaults
#
python /home/root/iot/customizations/edison_python/bluetooth/SPP-loopback.py &

if [ -f ~/iot/flags/run_python_on_startup.flag ]; then
	python /home/root/iot/customizations/edison_python/my_examples/01.Basics/blink.py
fi

