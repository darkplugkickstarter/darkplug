''' Code to control and show animation with onboard RGB WS2812b led, controlling with USER Button '''
import time
import board
import neopixel
import digitalio
import random
import math

# ---------------- Setup ----------------

pixel = neopixel.NeoPixel(board.GP10, 1, brightness=0.4, auto_write=True)

button = digitalio.DigitalInOut(board.GP1)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# ---------------- Variables ----------------

mode = "static"
brightness_levels = [0.2, 0.4, 0.7]
brightness_index = 1

current_color = (0, 0, 255)
pixel[0] = current_color

last_state = True
press_start = 0
last_press_time = 0
double_window = 0.4

cycle_step = 0
breathe_step = 0

# ---------------- Helpers ----------------

def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def startup_animation():
    for i in range(255):
        pixel[0] = (255 - i, i, 0)
        time.sleep(0.003)
    for i in range(255):
        pixel[0] = (0, 255 - i, i)
        time.sleep(0.003)
    for i in range(255):
        pixel[0] = (i, 0, 255 - i)
        time.sleep(0.003)

# ---------------- Startup ----------------

startup_animation()
pixel[0] = current_color

# ---------------- Main Loop ----------------

while True:
    current_state = button.value

    # Button pressed
    if last_state and not current_state:
        press_start = time.monotonic()

    # Button released
    if not last_state and current_state:
        duration = time.monotonic() - press_start

        if duration > 3:
            brightness_index = (brightness_index + 1) % len(brightness_levels)
            pixel.brightness = brightness_levels[brightness_index]

        elif duration > 1:
            mode = "breathe"

        else:
            if time.monotonic() - last_press_time < double_window:
                mode = "cycle"
            else:
                mode = "static"
                current_color = random_color()
                pixel[0] = current_color

            last_press_time = time.monotonic()

    last_state = current_state

    # -------- Non-Blocking Modes --------

    if mode == "cycle":
        cycle_step += 1
        r = int((math.sin(cycle_step * 0.05) + 1) * 127)
        g = int((math.sin(cycle_step * 0.05 + 2) + 1) * 127)
        b = int((math.sin(cycle_step * 0.05 + 4) + 1) * 127)
        pixel[0] = (r, g, b)

    elif mode == "breathe":
        breathe_step += 1
        brightness = (math.sin(breathe_step * 0.08) + 1) / 2
        pixel[0] = tuple(int(c * brightness) for c in current_color)

    time.sleep(0.01)
