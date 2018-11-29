from appscript import *
from datetime import datetime
from pathlib import Path
import copy

LOGFILE_DIR = "log/chromeTabCount.log"

def monitorTabCount():
    newChromeTabs = map(lambda x: x, app('Google Chrome').windows[0].tabs())
    count = 0
    for tab in newChromeTabs:
        count += 1

    # Append to file
    f = open(LOGFILE_DIR, "a+")
    f.write(str(count))
    f.close()


monitorTabCount()