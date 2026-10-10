''' Code to open any website -> Mac OS '''
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

# Open Spotlight (Cmd + Space)
keyboard.send(Keycode.GUI, Keycode.SPACE)
time.sleep(0.6)

# Type URL and Enter (Spotlight opens it in default browser)
layout.write("https://www.youtube.com/@kickstarter")
keyboard.send(Keycode.ENTER)

# Wait for page to load
time.sleep(5)

# Red: done
pixels[0] = (255, 0, 0)
