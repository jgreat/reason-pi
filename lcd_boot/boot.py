#!/usr/bin/python

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

def spinner(col, row):
    count = 0
    lcd.set_cursor(col, row)
    while count < 3:
        lcd.write8(ord('.'), True)
        time.sleep(0.75)
        count += 1
    lcd.set_cursor(col, row)
    lcd.message('   ')
    time.sleep(0.75)

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                              lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)


lcd.set_color(1.0, 0.0, 0.0)
lcd.clear()
lcd.home()
count = 0
while count < 5:
    spinner(4, 0)
    count += 1

# states = [
#     'Initializing',
#     'Ignite Reactor',
#     'Stablizing Reaction',
#     'Warming Up Rails',
#     'Ready'
# ]
#
# mes = '''
# NG Security Industries
#     REASON v0.1
# '''.strip()
# lcd.message(mes)
#
# for i, v in enumerate(states):
#     lcd.set_cursor(0, 3)
#     lcd.message(v)
#     count = 0
