# darkplug
DarkPlug is a compact, programmable USB-C development dongle built around the Raspberry Pi RP2350.
Designed for makers, developers, automation enthusiasts, and embedded hardware experimentation, DarkPlug turns a tiny USB-C device into a programmable platform for USB HID, automation, scripting, prototyping, and embedded development.

Plug it in. Write your code. Build something useful.

## ✨ Features
- 🚀 Raspberry Pi RP2350A
- 🔌 Direct USB-C connection
- ⌨️ USB HID support
- 🖱️ Keyboard and mouse emulation
- 🎮 Programmable USB input/control
- 🤖 Automation and macro applications
- 💡 On-board status indication
- 🛠️ CircuitPython, MicroPython and C/C++ development support
- 💻 Works with common desktop operating systems through standard USB HID
- 🔓 Designed for experimentation and customization
- 📦 Compact and portable design

At the heart of DarkPlug is the Raspberry Pi RP2350, which is Dual-core Arm Cortex-M33 processors supports Up to 150 MHz operation, 520 KB on-chip SRAM, Hardware SHA-256 acceleration and TrustZone security features.

DarkPlug can automate repetitive computer interactions using programmable USB HID actions.

For example:

```
Connect DarkPlug
      ↓
USB device detected 
      ↓
DarkPlug executes programmed sequence
      ↓
Keyboard / Mouse / HID actions
      ↓
Automation complete

```

The automation sequence can be completely customized in firmware.

### Hardware Pinout:
<img src="https://github.com/darkplugkickstarter/darkplug/blob/main/images/darkplug_pinout.png" weight="" height="">

### Getting Started with HackBee:
* Download and Install Thonny IDE from [here](https://thonny.org/)

  <img src="https://thonny.org/img/screenshot.png" weight="560" height="336">
* By default you will receive Hackbee device with Circuitpython pre-installed, so you can directly start using examples. Checkout [installation guide](https://github.com/hacktheboard/hackbee/blob/main/Documents/CircuitPython%20or%20MicroPython%20Installation.pdf) only if you want to re-install CircuitPython.
* When you connect device to PC/laptop, it will run defualt demo script and listed as CircuitPython folder as shown,

  <img src="https://github.com/darkplugkickstarter/darkplug/blob/main/images/circuitpython_device.png" weight="512" height="201">
  
  <img src="https://github.com/darkplugkickstarter/darkplug/blob/main/images/circuitpython_folder.png" weight="523" height="322">

#### Try Examples 
* Download complete github to try various sample codes provided here and you can modify to try different functionality

  <img src="https://github.com/darkplugkickstarter/darkplug/blob/main/images/git_download.png" weight="576" height="343">
  
* Open any example in thonny, select circuitpython device with COM Port and click Green Play button to run example as shown,

  <img src="https://github.com/darkplugkickstarter/darkplug/blob/main/images/select_device.png" weight="" height="">

  <img src="https://github.com/darkplugkickstarter/darkplug/blob/main/images/example_run.png" weight="" height="">

* For standalone exection save script to device as _**code.py**_

  <img src="https://github.com/darkplugkickstarter/darkplug/blob/main/images/code_1.png" weight="421" height="368">

  <img src="https://github.com/darkplugkickstarter/darkplug/blob/main/images/code_2.png" weight="408" height="301">

  <img src="https://github.com/darkplugkickstarter/darkplug/blob/main/images/code_3.png" weight="436" height="255">

#### Working Demonstration:
<img src="https://github.com/darkplugkickstarter/darkplug/blob/main/images/keylogger.gif" weight="" height="">

### Resources
- [RP2350 Datasheet](https://pip-assets.raspberrypi.com/categories/1214-rp2350/documents/RP-008373-DS-2-rp2350-datasheet.pdf)
- [Getting Started with Pico and CircuitPython](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/overview)
- [CircuitPython Documentation](https://docs.circuitpython.org/_/downloads/en/latest/pdf/)

DarkPlug is designed to encourage experimentation.
The goal is to provide developers and makers with the hardware, firmware examples, and documentation needed to understand how the device works and build their own applications.

As the project develops, this repository will become the central place for:

- Firmware
- Examples
- Hardware documentation
- Development resources
- Application notes
- Community contributions

🤝 Contributing :
Contributions, examples, improvements, and documentation updates are welcome.
If you have an idea for DarkPlug, feel free to open an issue or submit a pull request.


Designed by Affinity for makers, developers, and anyone who wants a programmable computer interface that fits in their pocket.
DarkPlug © Affinity
