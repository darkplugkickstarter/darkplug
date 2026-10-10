''' Code to open any website -> Windows OS '''
import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import neopixel

# NeoPixel on GP10
pixels = neopixel.NeoPixel(board.GP10, 1, brightness=0.5, auto_write=True)

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Turn RGB Green before opening website
pixels[0] = (0, 255, 0)  # Green
time.sleep(0.5)

# Open Run dialog (Win+R)
keyboard.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.2)

# Type YouTube URL and Enter
layout.write("https://www.youtube.com/@kickstarter")  # replace with your website
keyboard.send(Keycode.ENTER)

# Wait for the page to load
time.sleep(5)

# Turn RGB Red after website opened
pixels[0] = (255, 0, 0)  # Red
