import pandas as pd 

def windowTouchesCount():
    count = 0
    start = True
    windowContent = [line.strip() for line in open("./../log/windowAudit.log", 'r')]
    windowCount_feature = []
    for line in windowContent:
        if line != "":
            if "---5min Window Audit milestone" in line:
                if start:
                    start = False
                else:
                    windowCount_feature.append(count)
                    count = 0 
            else:
                count += 1
    df = pd.DataFrame(windowCount_feature, columns=['touched_windows_count'])
    df.to_csv("windows_touched_feature.csv", index=False, sep=' ')
    return 

windowTouchesCount()