#!/usr/bin/python

from gpiozero import Button
from signal import pause
import time


def on():
    print('Switch is On')


def off():
    print('Switch is Off')


key_switch = Button(pin=26)

key_switch.when_pressed = on
key_switch.when_released = off

pause()
