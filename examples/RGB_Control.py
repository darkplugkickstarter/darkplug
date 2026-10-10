''' Onboard RGB WS2812b control '''

import time
import board
import neopixel
import digitalio
import random

# ---------------- Setup ----------------

# NeoPixel on GP10
pixel = neopixel.NeoPixel(board.GP10, 1, brightness=0.4, auto_write=True)

# Button on GPIO1 (active LOW)
button = digitalio.DigitalInOut(board.GP1)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# ---------------- Start State ----------------

pixel[0] = (0, 0, 255)  # Blue at startup

last_state = True

# ---------------- Main Loop ----------------

while True:
    current_state = button.value

    # Detect button press (HIGH → LOW)
    if last_state and not current_state:
        pixel[0] = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        time.sleep(0.25)  # debounce delay

    last_state = current_state
    time.sleep(0.01)
