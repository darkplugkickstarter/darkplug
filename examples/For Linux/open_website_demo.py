''' Code to open any website -> Ubuntu OS '''
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

time.sleep(2)  # allow USB to enumerate

# Green: starting
pixels[0] = (0, 255, 0)
time.sleep(0.5)

# Open Terminal (Ctrl + Alt + T)
keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)
time.sleep(1)

# Open URL using xdg-open
layout.write("xdg-open https://www.youtube.com/@kickstarter\n")

# Wait for page to load
time.sleep(5)

# Red: done
pixels[0] = (255, 0, 0)
