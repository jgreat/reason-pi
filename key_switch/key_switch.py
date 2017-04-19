#!/usr/bin/python

from gpiozero import Button
from signal import pause
import time
from RPLCD import CharLCD

lcd = CharLCD()


def on(key_switch, lcd):
    print('Switch is On')
    # lcd.set_backlight(1)
    # lcd.set_color(1.0, 0.0, 0.0)
    lcd.clear()
    lcd.home()
    lcd.write_string(u'   REASON v1.0B7')
    lcd.cursor_pos(2, 0)
    lcd.write_string(u' Ng Security Indust.')
    lcd.set_cursor(3, 0)
    lcd.message(
        'PRERELEASE VERSION -- NOT FOR FIELD USE -- DO NOT TEST IN A POPULATED AREA -- READY TO FIRE --')

    lcd.set_cursor(0, 3)
    # while True:
    #     if key_switch.is_pressed:
    #         lcd.message(' ULTIMA RATIO REGUM')
    #         time.sleep(2)
    #         lcd.set_cursor(0, 3)
    #         lcd.message(' ' * 20)
    #         time.sleep(.5)
    #     else:
    #         break


def off(lcd):
    print('Switch is Off')
    lcd.clear()
    # lcd.set_backlight(0)


lcd.clear()
# lcd.set_backlight(0)
key_switch = Button(pin=26)
key_switch.when_pressed = on(key_switch, lcd)
key_switch.when_released = off(lcd)
pause()
