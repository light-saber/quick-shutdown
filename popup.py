#!/usr/bin/env python
#A simple script that checks the uptime and if it is greater than 15 hours, gives you an option to shut down the computer
#Trying out python scripts, thats all

#Created by light-saber
#Date: 2014.06.27

import os
import easygui
import math
from datetime import timedelta

with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
uptimes = uptime_seconds/3600
uptime=math.floor(uptimes)
if uptime > 15:
        message = "The computer is up and running for "+ str(uptime) +" hours"
        title = "Warning"
        if easygui.boolbox(message, title, ["Shutdown","Cancel"]):
                os.system("shutdown -h 10")
        else:
                pass
else:
        pass
