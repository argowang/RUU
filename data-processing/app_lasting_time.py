import time 
import datetime
import pandas as pd 

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end 
        self.lasting = 0

def unixTime_intervals(element):
    fromTime, toTime = element.split("--")
    # Conver to unix time
    fromTime = time.mktime(datetime.datetime.strptime(fromTime, "%Y-%m-%d-%H:%M:%S").timetuple()) 
    toTime = time.mktime(datetime.datetime.strptime(toTime, "%Y-%m-%d-%H:%M:%S").timetuple()) 
    return fromTime, toTime

def unixTime_windows(element):
    currentStart = element[:31]
    currentEnd = element[32:63]
    # Conver to Unix time
    currentStart = time.mktime(datetime.datetime.strptime(currentStart, "%I:%M:%S%p on %B %d, %Y").timetuple())
    currentEnd = time.mktime(datetime.datetime.strptime(currentEnd, "%I:%M:%S%p on %B %d, %Y").timetuple())
    return currentStart, currentEnd

def buildIntervalObject(dataList):
    intervals = []
    for line in dataList:
        start, end = unixTime_intervals(line)
        intervals.append(Interval(start, end))
    return intervals

def buildWindowObject(dataList):
    intervals = []
    for line in dataList:
        start, end = unixTime_windows(line)
        intervals.append(Interval(start, end))
    return intervals

def lastingTimeRatio(appName):
    # Get interval template's time
    raw_intervals = pd.read_csv("interval_template.csv")
    raw_intervals = pd.DataFrame(raw_intervals)
    # package to Interval object
    intervals = buildIntervalObject(raw_intervals.time_intervals)
    
    # clean up windows log
    windowContent = [line.strip() for line in open("./../log/test.log", 'r')]
    windowContent = [line for line in windowContent if line != "" and "---5min Window Audit milestone" not in line and appName in line]
    # package to Interval object
    appBucket = buildWindowObject(windowContent)

        
    # Two pointers
    i, j = 0, 0
    appLastingTime_ratio = []
    current = appBucket[0]
    while j < len(appBucket) and i < len(intervals):  
        inv = intervals[i]
        if current.start > inv.end:
            i += 1
            appLastingTime_ratio.append(inv.lasting * 1.0 / (inv.end - inv.start))
        else:
            if current.end <= inv.end:
                j += 1
                inv.lasting += (current.end - current.start)
                if j < len(appBucket):
                    current = appBucket[j]
            else:
                inv.lasting += (inv.end - current.start) 
                current.start = inv.end
                i += 1
                appLastingTime_ratio.append(inv.lasting * 1.0 / (inv.end - inv.start))

    # Traverse the rest time intervals
    while i < len(intervals):
        inv = intervals[i]
        appLastingTime_ratio.append(inv.lasting * 1.0 / (inv.end - inv.start))
        i += 1
    
    df = pd.DataFrame(appLastingTime_ratio, columns=[appName + '_count'])
    df.to_csv(appName + "_count_feature.csv", index=False, sep=' ')
    return appLastingTime_ratio

lastingTimeRatio("Google Chrome")