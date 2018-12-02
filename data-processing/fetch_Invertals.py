import pandas as pd
import time
import datetime

# Get intermediate file
import subprocess
bashCommand = '''echo "time" > interval_intermediate.csv && cat ../log/keyStroke.log | grep "\-\-\-5min" | grep -o '[0-9]*-[0-9]*-[0-9]*-[0-9]*:[0-9]*:[0-9]*' >> ./../data_processing/interval_intermediate.csv'''
subprocess.check_output(bashCommand, shell=True)


raw_time = pd.read_csv("interval_intermediate.csv")
raw_time = pd.DataFrame(raw_time)

all_time_stamp = []
dateTime = str(raw_time.time[0])
unixTime = time.mktime(datetime.datetime.strptime(dateTime, "%Y-%m-%d-%H:%M:%S").timetuple())
for i in range(1,len(raw_time.time)):
    new_unixTime = time.mktime(datetime.datetime.strptime(str(raw_time.time[i]), "%Y-%m-%d-%H:%M:%S").timetuple())
#     if (new_unixTime - unixTime) >= 300 and (new_unixTime - unixTime) <= 305:
#         
    all_time_stamp.append(datetime.datetime.fromtimestamp(unixTime).strftime('%Y-%m-%d-%H:%M:%S')+"--"+datetime.datetime.fromtimestamp(new_unixTime).strftime('%Y-%m-%d-%H:%M:%S'))
    unixTime = new_unixTime
df = pd.DataFrame(all_time_stamp, columns=['time_intervals'])
df.to_csv("interval_template.csv", index=False, sep=' ')