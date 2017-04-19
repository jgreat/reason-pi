#!/usr/bin/python

from gpiozero import Button
from signal import pause
import time
import Adafruit_CharLCD as LCD

# Raspberry Pi configuration:
lcd_rs = 27  # Change this to pin 21 on older revision Raspberry Pi's
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_red = 4
lcd_green = 17
lcd_blue = 7  # Pin 7 is CE1

# Alternatively specify a 20x4 LCD.
lcd_columns = 20
lcd_rows = 4

boot_message = '''
   REASON v1.0B7
 Ng Security Indst.
 ULTIMA RATIO REGUM
'''

lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                              lcd_d7, lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)
lcd.enable_display(False)


def on():
    print('Switch is On')
    lcd.enable_display(True)
    lcd.set_color(1.0, 0.0, 0.0)
    lcd.clear()
    lcd.home()
    lcd.message(boot_message.strip)


def off():
    print('Switch is Off')
    lcd.clear()
    lcd.enable_display(False)


key_switch = Button(pin=26)
key_switch.when_pressed = on
key_switch.when_released = off
pause()
