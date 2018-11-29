from appscript import *
from datetime import datetime
from pathlib import Path
import copy

class appSensor(object):
    def __init__(self, timeRange=1):
        self.chromeTabNum = 0
        self.currentSecond = datetime.now()
        self.oldChromeTabsSet = set()

        while True:
            now = datetime.now()
            if int((now - self.currentSecond).seconds) >= timeRange:
                self.monitorChromeTabNum()
                self.currentSecond = now


    def monitorChromeTabNum(self):
        self.startTime = datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        self.newChromeTabs = map(lambda x: x, app('Google Chrome').windows[0].tabs())
        self.newChromeTabsSet = set()

        update = ""
        for tab in self.newChromeTabs:
            if tab.id() not in self.oldChromeTabsSet:
                update += self.startTime + " open " + str(tab.id()) + " " + tab.title() + "\n"
            self.newChromeTabsSet.add(tab.id())
        for oldTab in self.oldChromeTabsSet:
            if oldTab not in self.newChromeTabsSet:
                update += self.startTime + " close " + str(tab.id()) + " " + oldTab.title() + "\n"

        # Append to file
        windowSensorFile = Path("appSensor.txt")
        if not windowSensorFile.is_file():
            f = open("appSensor.txt", "w")
            f.write("startTime operation id activeAppName \n")
            f.close()
        f = open("appSensor.txt", "a")
        f.write(update)
        f.close()
        self.oldChromeTabsSet = copy.copy(self.newChromeTabsSet)
        self.newChromeTabsSet = set()


appSensor()