# 10moons-t503-driver

[简体中文](https://github.com/calico-cat-3333/10moons-t503-driver/blob/master/README_zh.md)

Simple driver for 10moons T503 tablet for linux

## About

Driver which provides basic functionality for 10moons T503 tablet:
* 4 buttons on the tablet itself
* Correct X and Y positioning
* Pressure sensitivity
* 2 buttons on the pen (See "Buttons on the Pen" section below)
* Screen Mapping

Tablet has 4080 levels in both axes and 2047 levels of pressure.

## Buttons on the Pen

Buttons on the pen works fine on my device, but I can't guarantee that it will work fine on yours.

The second button on the pen (with a '-' on it) can be configured with the official Windows driver, changing the configuration will make this driver not detect this button. So, if this driver does not detect this button, you can open the configuration program on Windows and reset this button to its default value.

## How to use

Clone or download this repository.

```
git clone https://github.com/calico-cat-3333/10moons-t503-driver.git
```

Then install all dependencies listed in _requirements.txt_ file either using python virtual environments or not.

```
python3 -m pip install -r requirements.txt
```

For Debian or Ubuntu users, you can also use apt to install all dependencies.

```
sudo apt install python3-evdev python3-usb python3-yaml
```

Connect tablet to your computer and then run _driver.py_ file with sudo privileges.

```
sudo python3 driver.py
```

**You need to connect your tablet and run the driver prior to launching a drawing software otherwise the device will not be recognized by it.**

## Configuring tablet

Configuration of the driver placed in _config.yaml_ file.

### VID & PID

You may need to change the *vendor_id* and the *product_id* but I'm not sure (You device can have the same values as mine, but if it is not you can run the *lsusb* command to find yours).

### Buttons

The first four of *tablet_buttons* will be assigned to the buttons on the tablet in left-to-right order, and the last two will be assigned to the two buttons on the pen. You can assign to them any button on the keyboard and their combinations separating them with a plus (+) sign.

To list all the possible key codes you may run:
```
python3 -c "from evdev import ecodes; print([x for x in dir(ecodes) if 'KEY' in x])"
```

### Swap Axis or Directions

If you find that using this driver with your tablet results in reverse axis or directions (or both), you can modify parameters *swap_axis*, *swap_direction_x*, and *swap_direction_y* by changing false to true and another way around.

### Screen Mapping

The 4 parameters are used to map the screen to the tablet, all values are in percent.
* *width_percent* is the width of the mapped area.
* *height_percent* is the height of the mapped area.
* *x_offset_percent* is the horizontal distance of the top left corner of the mapped area relative to the top left corner of the screen.
* *y_offset_percent* is the vertical distance of the top left corner of the mapped area relative to the top left corner of the screen.

Their relationship is shown in the figure below.

![screen_mapping.png](screen_mapping.png)

A simple program for generating screen mapping parameters is also provided. Run:

```
python3 screen_mapping_config.py
```

Then use the mouse to select an area, just like the screenshot tool does. The screen mapping parameters for the selected area can then be obtained from the terminal output.

## Credits

Some parts of code are taken from: https://github.com/Mantaseus/Huion_Kamvas_Linux

## Known issues

~~Buttons on the pen itself do not work and hence not specified. I don't know if it's the issue only on my device or it's a common problem.~~
