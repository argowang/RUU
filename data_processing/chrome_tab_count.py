import pandas as pd 

def chromeTabCount():
    chromeTabCountContent = [line.strip() for line in open("./../log/chromeTabCount.log", 'r')]
    chromeTabCountContent = [line for line in windowContent if line != "" and "---5min Chrome Tab Count Audit milestone" not in line and "Google Chrome" in line]
    df = pd.DataFrame(chromeTabCountContent, columns=['chrome_tab_count'])
    df.to_csv("chrome_tab_count_feature.csv", index=False, sep=' ')
    return 
    