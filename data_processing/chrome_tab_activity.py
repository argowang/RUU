import pandas as pd

def chromeTabOpen():
    chromeTabActContent = [line.strip() for line in open("./../log/chromeTab.log", 'r')]
    openAct = []
    start = True
    count = 0
    for line in chromeTabActContent:
        if "---5min Chrome Tab Audit milestone" in line:
            # Ignore the first line
            if start:
                start = False
            else:
                openAct.append(count)
                count = 0
        elif "open" in line:
            count += 1
    openAct.append(count)
        
    df = pd.DataFrame(openAct, columns=['chrome_tab_open_act'])
    df.to_csv("chrome_tab_open_feature.csv", index=False, sep=' ')
    return  

def chromeTabClose():
    chromeTabActContent = [line.strip() for line in open("./../log/chromeTab.log", 'r')]
    openAct = []
    start = True
    count = 0
    for line in chromeTabActContent:
        if "---5min Chrome Tab Audit milestone" in line:
            # Ignore the first line
            if start:
                start = False
            else:
                openAct.append(count)
                count = 0
        elif "close" in line:
            count += 1
    openAct.append(count)
        
    df = pd.DataFrame(openAct, columns=['chrome_tab_close_act'])
    df.to_csv("chrome_tab_close_feature.csv", index=False, sep=' ')
    return 