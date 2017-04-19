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

lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                              lcd_d7, lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)


def scroll(lcd, text, pause1=False, pause2=False, rep=False):
    PAUSE_NEXT = 2
    PAUSE_REP = 2
    REPETITIONS = 4

    if pause1:
        PAUSE_NEXT = pause1
    if pause2:
        PAUSE_REP = pause2
    if rep:
        REPETITIONS = rep

    n = 20
    rows = [text[i:i + n] for i in range(0, len(text), n)]
    n_rows = len(rows)
    for i in range(REPETITIONS):
        for x in range(n_rows):
            lcd.home()
            lcd.clear()
            nxt = x + 1
            lcd.message(rows[x] + "\n")
            if nxt == n_rows:
                time.sleep(2)

                break
            else:
                lcd.message(rows[nxt])
                time.sleep(PAUSE_REP)

    lcd.clear()


def on(key_switch, lcd):
    print('Switch is On')
    lcd.set_backlight(1)
    lcd.set_color(1.0, 0.0, 0.0)
    lcd.clear()
    lcd.home()
    lcd.message('   REASON v1.0B7')
    lcd.set_cursor(0, 1)
    lcd.message(' Ng Security Indust.')
    lcd.set_cursor(0, 2)
    lcd.message(
        'PRERELEASE VERSION -- NOT FOR FIELD USE -- DO NOT TEST IN A POPULATED AREA -- READY TO FIRE --')

    lcd.set_cursor(0, 3)
    while True:
        if key_switch.is_pressed:
            lcd.message(' ULTIMA RATIO REGUM')
            time.sleep(2)
            lcd.set_cursor(0, 3)
            lcd.message(' ' * 20)
            time.sleep(.5)
        else:
            break


def off(lcd):
    print('Switch is Off')
    lcd.clear()
    lcd.set_backlight(0)


lcd.clear()
lcd.set_backlight(0)
key_switch = Button(pin=26)
key_switch.when_pressed = on(key_switch, lcd)
key_switch.when_released = off(lcd)
pause()
