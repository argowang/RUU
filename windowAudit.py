from AppKit import NSWorkspace
from datetime import datetime
import time
from pathlib import Path
from Quartz import (
        CGWindowListCopyWindowInfo,
        kCGWindowListOptionOnScreenOnly,
        kCGNullWindowID
    )

class windowSensor(object):
    def __init__(self, timeRange=0.2):
        self.start = ""
        self.end = ""
        self.activeAppName = ""
        self.currentSecond = datetime.now()
        while True:
            now = datetime.now()
            if int((now - self.currentSecond).seconds) >= timeRange:
                self.monitor()
                self.currentSecond = now


    def monitor(self):
        new_active_app_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        # Write to File
        windowSensorFile = Path("windowSensor.txt")
        if not windowSensorFile.is_file():
            f = open("windowSensor.txt", "w")
            f.write("startTime endTime activeAppName\n")
            f.close()
        if new_active_app_name != self.activeAppName:
            if self.activeAppName != "":
                self.start = self.end
                self.end = datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
                f = open("windowSensor.txt", "a")
                line = self.start + " " + self.end + " " + self.activeAppName + "\n"
                f.write(line)
                f.close()
                time.sleep(0.01)
        self.activeAppName = new_active_app_name


windowSensor()