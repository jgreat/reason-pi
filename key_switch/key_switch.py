#!/bin/env python

from gpiozero import Button
import time

key_switch = Button(pin=26)

while true:
    if key_switch.is_pressed:
        print('Switch is On')
    else:
        print('Seitch is Off')
    time.sleep(1)
