from appscript import *
from datetime import datetime
from pathlib import Path
import copy

LOGFILE_DIR = "log/chromeTabCount.log"

class tabCountSensor(object):
    def __init__(self, timeRange=3):
        self.currentSecond = datetime.now()

        while True:
            now = datetime.now()
            if int((now - self.currentSecond).seconds) >= timeRange:
                self.monitorTabCount()
                self.currentSecond = now


    def monitorTabCount(self):
        self.newChromeTabs = map(lambda x: x, app('Google Chrome').windows[0].tabs())
        count = 0
        update = ""
        for tab in self.newChromeTabs:
            count += 1
        update += str(count) + "\n"

        # Append to file
        f = open(LOGFILE_DIR, "a")
        f.write(update)
        f.close()


tabCountSensor()