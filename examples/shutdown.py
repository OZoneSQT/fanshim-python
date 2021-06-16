#!/usr/bin/env python3
import signal, os
from fanshim import FanShim

fanshim = FanShim()

# Set time for long press on button to 2 sec
fanshim.set_hold_time(2.0)

# control for button on FansHim fan hat
@fanshim_on_release()
def releade_handler(was_held):
    if was_held: 
      # system shutdown, on long press
      os.system("sudo shutdown")
    else:
      # system reboot, on short press
      os.system("sudo reboot")

try:
    signal.pause()
except KeyboardInterrupt:
    pass
