# Fan Shim for Raspberry Pi

[![Build Status](https://travis-ci.com/pimoroni/fanshim-python.svg?branch=master)](https://travis-ci.com/pimoroni/fanshim-python)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/fanshim-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/fanshim-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/fanshim.svg)](https://pypi.python.org/pypi/fanshim)
[![Python Versions](https://img.shields.io/pypi/pyversions/fanshim.svg)](https://pypi.python.org/pypi/fanshim)

# Installing

Stable library from PyPi:

* Just run `sudo pip install fanshim`

Latest/development library from GitHub:

* `git clone https://github.com/OZoneSQT/fanshim-python`
* `cd fanshim-python`
* `sudo ./install.sh`

# Reference

You should first set up an instance of the `FANShim` class, eg:

```python
from fanshim import FanShim
fanshim = FanShim()
```

## Fan

Turn the fan on with:

```python
fanshim.set_fan(True)
```

Turn it off with:

```python
fanshim.set_fan(False)
```

You can also toggle the fan with:

```python
fanshim.toggle_fan()
```

You can check the status of the fan with:

```python
fanshim.get_fan() # returns 1 for 'on', 0 for 'off'
```

## LED

Fan Shim includes one RGB APA-102 LED.

Set it to any colour with:

```python
fanshim.set_light(r, g, b)
```

Arguments r, g and b should be numbers between 0 and 255 that describe the colour you want.

For example, full red:

```
fanshim.set_light(255, 0, 0)
```

## Button

Fan Shim includes a button, you can bind actions to press, release and hold events.

Do something when the button is pressed:

```python
@fanshim.on_press()
def button_pressed():
    print("The button has been pressed!")
```

Or when it has been released:

```python
@fanshim.on_release()
def button_released(was_held):
    print("The button has been pressed!")
```

Or when it's been pressed long enough to trigger a hold:

```python
fanshim.set_hold_time(2.0)

@fanshim.on_hold()
def button_held():
    print("The button was held for 2 seconds")
```

The function you bind to `on_release()` is passed a `was_held` parameter,
this lets you know if the button was held down for longer than the configured
hold time. If you want to bind an action to "press" and another to "hold" you
should check this flag and perform your action in the `on_release()` handler:

```python
@fanshim.on_release()
def button_released(was_held):
    if was_held:
        print("Long press!")
    else:
        print("Short press!")
```

To configure the amount of time the button should be held (in seconds), use:

```python
fanshim.set_hold_time(number_of_seconds)
```

If you need to stop Fan Shim from polling the button, use:

```python
fanshim.stop_polling()
```

You can start it again with:

```python
fanshim.start_polling()
```

## Cron job, to run script on startup

This part, is what i wished Google told me, when learning about cron job's
To add reboot/shutdown function to the button, you can follow this section:

Edit crontab file, or create one if it doesn’t already exist.

```python
crontab -e
```

Then select "nano" as editing tool, navigate to the bottum of the file, 
where you add a line. Remember write "python3" when you use Python 3 
and "python" if you are using python 2.x:

```python
@reboot python3 /home/pi/fanshim-python/examples/shutdown.py &
```

Press [ctrl] + [x] to exit the crontab file, then press [y] to 
confirm the changes to the file.

Then restart the system by pressing [esc] and 
returning to the terminal window.

```python
sudo reboot
```
