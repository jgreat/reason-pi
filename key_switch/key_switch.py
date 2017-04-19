#!/usr/bin/python

from gpiozero import Button
from signal import pause
import time
#import Adafruit_CharLCD as LCD

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


# def write_to_lcd(lcd, framebuffer, num_cols):
#     lcd.home()
#     for row in framebuffer:
#         lcd.message(row.ljust(num_cols)[:num_cols])
#         lcd.message('\n')


def on():
    print('Switch is On')
    # lcd.set_backlight(1)
    # lcd.set_color(1.0, 0.0, 0.0)
    # lcd.clear()
    # framebuffer = [
    #     '   REASON v1.0B7',
    #     ' Ng Security Indust.',
    #     ' ',
    #     ' '
    # ]
    # write_to_lcd(lcd, framebuffer, 20)
    # long_string = 'PRERELEASE VERSION -- NOT FOR FIELD USE -- DO NOT TEST IN A POPULATED AREA -- READY TO FIRE --'
    # for i in range(len(long_string) - 20 + 1):
    #     framebuffer[2] = long_string[i:i + 20]
    #     write_to_lcd(lcd, framebuffer, 20)
    #     time.sleep(0.2)

    # lcd.message('   REASON v1.0B7')
    # lcd.set_cursor(0, 1)
    # lcd.message(' Ng Security Indust.')
    # lcd.set_cursor(0, 2)
    # lcd.message(
    #     'PRERELEASE VERSION -- NOT FOR FIELD USE -- DO NOT TEST IN A POPULATED AREA -- READY TO FIRE --')
    #
    # lcd.set_cursor(0, 3)
    # while True:
    #     if key_switch.is_pressed:
    #         lcd.message(' ULTIMA RATIO REGUM')
    #         time.sleep(2)
    #         lcd.set_cursor(0, 3)
    #         lcd.message(' ' * 20)
    #         time.sleep(.5)
    #     else:
    #         break


def off():
    print('Switch is Off')
    # lcd.clear()
    # lcd.set_backlight(0)


with Button(26) as key_switch:
    # lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
    #   lcd_d7, lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)

    # lcd.clear()
    # lcd.set_backlight(0)
    lcd = 0
    key_switch.when_pressed = on()
    key_switch.when_released = off()
    pause()
