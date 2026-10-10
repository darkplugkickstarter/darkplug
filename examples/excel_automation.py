"""
HKBee Excel HID Demo: automatically open Excel, create a student marks table with formulas
Demonstrates USB HID keyboard automation with RGB status indication.
"""

import time
import board
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# ------------------ Setup ------------------
pixels = neopixel.NeoPixel(board.GP10, 1, brightness=0.4, auto_write=True)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def type_slow(text, delay=0.03):
    for c in text:
        layout.write(c)
        time.sleep(delay)

def press(*keys):
    keyboard.send(*keys)
    time.sleep(0.2)

# ------------------ Start ------------------
pixels[0] = (0, 255, 0)  # Green = Booting
time.sleep(3)

# ------------------ Open Run ------------------
press(Keycode.GUI, Keycode.R)
time.sleep(1)

# ------------------ Open Excel ------------------
pixels[0] = (0, 0, 255)  # Blue = Opening Excel
type_slow("excel")
press(Keycode.ENTER)

time.sleep(5)

# ------------------ Headers ------------------
headers = ["Roll No", "Name", "Math", "Physics", "Chemistry",
           "Total", "Percentage", "Grade"]

for header in headers:
    type_slow(header)
    press(Keycode.TAB)

press(Keycode.ENTER)

# ------------------ 10 Student Records ------------------
students = [
    (1, "Alice", 78, 82, 69),
    (2, "Bob", 55, 61, 70),
    (3, "Charlie", 90, 88, 92),
    (4, "David", 40, 52, 48),
    (5, "Eva", 67, 73, 70),
    (6, "Frank", 85, 79, 88),
    (7, "Grace", 91, 87, 84),
    (8, "Henry", 60, 65, 58),
    (9, "Ivy", 72, 68, 75),
    (10, "Jack", 49, 55, 60),
]

row_number = 2

for roll, name, m, p, c in students:

    # Basic Data
    type_slow(str(roll)); press(Keycode.TAB)
    type_slow(name); press(Keycode.TAB)
    type_slow(str(m)); press(Keycode.TAB)
    type_slow(str(p)); press(Keycode.TAB)
    type_slow(str(c)); press(Keycode.TAB)

    # Total Formula
    type_slow(f"=SUM(C{row_number}:E{row_number})")
    press(Keycode.TAB)

    # Percentage Formula
    type_slow(f"=F{row_number}/300*100")
    press(Keycode.TAB)

    # Grade Formula
    type_slow(
        f'=IF(G{row_number}>=75,"A",'
        f'IF(G{row_number}>=60,"B",'
        f'IF(G{row_number}>=50,"C",'
        f'IF(G{row_number}>=35,"D","F"))))'
    )

    press(Keycode.ENTER)
    row_number += 1

# ------------------ Finish ------------------
pixels[0] = (255, 0, 0)  # Red = Done

while True:
    pass
