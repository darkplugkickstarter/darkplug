"""
Educational CircuitPython HID demo:
Triggers Ubuntu shutdown or restart using keyboard automation.
Use only on machines you own or have permission to control.
"""

import time
import board
import usb_hid
import neopixel
import random

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# --- CONFIG ---
MODE = "restart"   # "shutdown" or "restart"

# --- Setup ---
pixels = neopixel.NeoPixel(board.GP10, 1, brightness=0.5, auto_write=True)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def set_color(c):
    pixels[0] = c

def blink(c, times=2, on=0.15, off=0.1):
    for _ in range(times):
        set_color(c)
        time.sleep(on)
        set_color((0,0,0))
        time.sleep(off)

def press(*keys):
    keyboard.send(*keys)
    time.sleep(0.15)

time.sleep(2)  # USB enumerate

# Ready indicator
blink((255, 200, 0), 3)

# Open Terminal (Ctrl + Alt + T)
press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
time.sleep(1.5)

# Choose command
if MODE == "restart":
    cmd = "shutdown -r now\n"
else:
    cmd = "shutdown -h now\n"

# Warning indicator
set_color((255, 0, 0))

# Type command
layout.write(cmd)

# End
time.sleep(1)
set_color((0, 0, 0))
