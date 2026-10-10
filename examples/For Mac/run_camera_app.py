''' Only Ethical and Educational Demo purpose, Open camera application -> Mac OS '''

import time
import board
import usb_hid
import neopixel

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# NeoPixel on GP10
pixels = neopixel.NeoPixel(board.GP10, 1, brightness=0.5, auto_write=True)

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def blink(color, t=0.3):
    pixels[0] = color
    time.sleep(t)
    pixels[0] = (0, 0, 0)
    time.sleep(0.2)

time.sleep(2)  # USB enumerate

# Starting
blink((255, 255, 0), 0.5)  # Yellow

# Open Spotlight (Cmd + Space)
keyboard.send(Keycode.GUI, Keycode.SPACE)
time.sleep(0.6)

# Launch Photo Booth
pixels[0] = (0, 255, 0)  # Green
layout.write("Photo Booth")
time.sleep(0.3)
keyboard.send(Keycode.ENTER)

# Wait for app to open
time.sleep(3)

# Indicate "recording" (manual in Photo Booth)
pixels[0] = (255, 0, 0)  # Red
time.sleep(5)

# Done
pixels[0] = (0, 0, 0)
