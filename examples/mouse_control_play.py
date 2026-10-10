'''
Mouse control Demo - Patterns Square, circle, spiral, sinewave
Press User button to start/stop Demo
'''
import time
import math
import board
import usb_hid
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.mouse import Mouse

# ---------------- Setup ----------------
pixels = neopixel.NeoPixel(board.GP10, 1, brightness=0.5, auto_write=True)
mouse = Mouse(usb_hid.devices)

button = DigitalInOut(board.GP1)
button.direction = Direction.INPUT
button.pull = Pull.UP

running = False
last_button_state = True

# ---------------- Helpers ----------------
def blink(color):
    pixels[0] = color
    time.sleep(0.01)
    pixels[0] = (0, 0, 0)

def move_step(dx, dy, color, delay=0.005):
    global running
    if not running:
        return False
    mouse.move(x=dx, y=dy)
    blink(color)
    time.sleep(delay)
    return True

def check_button():
    global running, last_button_state
    current = button.value

    if last_button_state and not current:
        running = not running
        time.sleep(0.3)  # debounce

        if running:
            pixels[0] = (0, 255, 0)  # briefly green before run
            time.sleep(0.3)
        else:
            pixels[0] = (255, 0, 0)  # red stop
            time.sleep(0.5)
            pixels[0] = (0, 255, 0)  # back to ready

    last_button_state = current

# Wait USB
pixels[0] = (255, 255, 255)
time.sleep(3)
pixels[0] = (0, 255, 0)  # Green ready

# =====================================================
# 1️⃣ Medium Square
# =====================================================
def square_pattern(size=500, step=6):
    color = (255, 0, 0)
    steps = size // step

    for _ in range(steps):
        if not move_step(step, 0, color): return
        check_button()
    for _ in range(steps):
        if not move_step(0, step, color): return
        check_button()
    for _ in range(steps):
        if not move_step(-step, 0, color): return
        check_button()
    for _ in range(steps):
        if not move_step(0, -step, color): return
        check_button()

# =====================================================
# 2️⃣ Medium Circle
# =====================================================
def circle_pattern(radius=250, resolution=120):
    color = (0, 255, 0)
    prev_x = 0
    prev_y = 0

    for i in range(resolution + 1):
        if not running: return
        angle = 2 * math.pi * i / resolution
        x = int(radius * math.cos(angle))
        y = int(radius * math.sin(angle))

        dx = x - prev_x
        dy = y - prev_y

        if not move_step(dx, dy, color): return

        prev_x = x
        prev_y = y
        check_button()

# =====================================================
# 3️⃣ Medium Spiral
# =====================================================
def spiral_pattern(max_radius=300, turns=4):
    color = (0, 0, 255)
    steps = 400
    prev_x = 0
    prev_y = 0

    for i in range(steps):
        if not running: return
        angle = 2 * math.pi * turns * i / steps
        radius = max_radius * i / steps

        x = int(radius * math.cos(angle))
        y = int(radius * math.sin(angle))

        dx = x - prev_x
        dy = y - prev_y

        if not move_step(dx, dy, color): return

        prev_x = x
        prev_y = y
        check_button()

# =====================================================
# 4️⃣ Medium Sine Wave
# =====================================================
def sine_wave_pattern(length=800, amplitude=150):
    color = (180, 0, 255)
    prev_y = 0

    for x in range(length):
        if not running: return
        y = int(amplitude * math.sin(x * 0.02))
        dy = y - prev_y

        if not move_step(2, dy, color): return

        prev_y = y
        check_button()

# =====================================================
# MAIN LOOP
# =====================================================
while True:
    check_button()

    if running:
        square_pattern()
        circle_pattern()
        spiral_pattern()
        sine_wave_pattern()
