#!/usr/bin/env python2

import psutil
import time
from datetime import datetime

# once this script is called, the pids of current moment would be appended to processLog.txt
def getPIDS():
    unixTime = time.time()
    formatTime = datetime.utcfromtimestamp(unixTime).strftime('%Y-%m-%d-%H:%M:%S')
    pids = psutil.pids()
    f = open("log/processLog.txt", "a+")
    f.write(str(unixTime) + " " + formatTime + " "+ " ".join(str(x) for x in pids) + "\n")
    f.close()

getPIDS()
