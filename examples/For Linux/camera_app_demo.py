''' Only Ethical and Educational Demo purpose - Open camera application '''
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
blink((255, 255, 0), 0.5)

# Open Terminal (Ctrl + Alt + T)
keyboard.send(Keycode.CONTROL, Keycode.ALT, Keycode.T)
time.sleep(1)

# Launch Cheese Camera
pixels[0] = (0, 255, 0)  # Green
layout.write("cheese\n")

# Wait for app
time.sleep(3)

# Indicate recording (Cheese usually needs mouse)
pixels[0] = (255, 0, 0)  # Red
time.sleep(5)

# Done
pixels[0] = (0, 0, 0)
