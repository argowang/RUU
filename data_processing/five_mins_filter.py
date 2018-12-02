# Concatenate features
def concatenate(fileList, outputFileName):
    import pandas as pd

    dfs = []
    for filename in fileList:
        # read the csv, making sure the first two columns are str
        df = pd.read_csv(filename, header=None, converters={0: str, 1: str})
        # throw away all but the first two columns
        df = df.ix[:,:1]
        # change the column names so they won't collide during concatenation
        df.columns = [filename + str(cname) for cname in df.columns]
        dfs.append(df)

    # concatenate them horizontally
    merged = pd.concat(dfs,axis=1)
    # write it out
    merged.to_csv(outputFileName, header=None, index=None)
    return 


# concatenate(["test1.csv", "test2.csv", "test3.csv"])

def filter(inputFile, outputFile):
    import time
    import datetime
    def unixTime_intervals(element):
        fromTime, toTime = element[:40].split("--")
        # Conver to unix time
        fromTime = time.mktime(datetime.datetime.strptime(fromTime, "%Y-%m-%d-%H:%M:%S").timetuple()) 
        toTime = time.mktime(datetime.datetime.strptime(toTime, "%Y-%m-%d-%H:%M:%S").timetuple()) 
        return fromTime, toTime
    
    inputFile = [line.strip() for line in open("./../data_processing/"+inputFile, 'r')]
#     output = []
    for line in inputFile[1:]:
        fromTime, toTime = unixTime_intervals(line)
        if (toTime - fromTime) >= 300 and (toTime - fromTime) <= 305:
            f = open(outputFile, "a+")
            f.write(line+"\n")
            f.close() 
    return

# concatenate(["test1.csv", "test2.csv", "test3.csv"], "features_intermediate.csv")
# filter("features_intermediate.csv", "final_fetures_file.csv")

