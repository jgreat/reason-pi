#!/bin/python

from gpiozero import Button
from signal import pause
import time


def on():
    print('Switch is On')


def off():
    print('Switch is Off')


key_switch = Button(pin=26)

button.when_pressed = on
button.when_released = off

pause()
