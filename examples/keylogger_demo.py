import time
import board
import neopixel
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# ---------------- Setup ----------------

# NeoPixel (on-board RGB LED)
pixel = neopixel.NeoPixel(board.GP10, 1, brightness=0.3, auto_write=True)

# Button on GPIO1 (active LOW)
button = digitalio.DigitalInOut(board.GP1)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# USB Keyboard
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# ---------------- Helpers ----------------

def set_color(color):
    pixel[0] = color

# ---------------- Startup ----------------

time.sleep(2)                 # Allow USB to enumerate
set_color((0, 0, 255))        # Blue: idle / ready

last_button_state = True

# ---------------- Main Loop ----------------

while True:
    current_state = button.value

    # Detect button press
    if last_button_state and not current_state:
        set_color((255, 0, 0))    # Red: typing

        layout.write("Demo1234")
        keyboard.send(Keycode.ENTER)

        time.sleep(0.3)
        set_color((0, 0, 255))    # Blue: idle

        time.sleep(0.3)          # debounce

    last_button_state = current_state
    time.sleep(0.01)
