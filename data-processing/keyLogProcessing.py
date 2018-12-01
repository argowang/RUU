import re

LOG_DIR = "../log_backup"

def splitByMilestone(inputList):    
    copy = False
    buffer = ""
    splitByMilestone = []
    for line in keyStrokeContent:
        if "---5min KeyLogger milestone" in line:
            copy = True
            splitByMilestone.append(buffer)
            buffer = ""
        if copy:
            buffer += line
    splitByMilestone = splitByMilestone[1:]
    return splitByMilestone

def countCmdTabCombo(input):
    pattern = re.compile("\[left-cmd\]\[tab\]")
    count = len(pattern.findall(input))
    return count

def countCmdNumber(input):
    pattern = re.compile("\[left-cmd\]")
    count = len(pattern.findall(input))
    return count

def calAverageTypingSpeed(input):
    copy = False
    buffer = ""
    splitByMilestone = []
    for line in input.split("\n"):
        if "***5s KeyLogger Milestone***" in line:
            copy = True
            splitByMilestone.append(buffer)
            buffer = ""
            continue
        if copy:
            buffer += line
    typingSpeed = []
    for line in splitByMilestone:
        if line == '':
            continue
        pattern = re.compile('\[.*?\]', re.IGNORECASE)
        cleanedLine, commandNum = pattern.subn("", line)
        keyNum = len(cleanedLine) + commandNum
        typingSpeed.append(keyNum * 1.0 / 5)
    if len(typingSpeed) == 0:
        return 0
    return round(reduce(lambda x, y: x + y, typingSpeed) / len(typingSpeed), 2)

keyStrokeFile = open(LOG_DIR+"/keyStroke.txt", "r")
keyStrokeContent = keyStrokeFile.readlines()

# clean up the content
keyStrokeContent = [line for line in keyStrokeContent if line != "\n" and line != "Keystrokes are now being recorded\n"]
keyStrokeContentRaw = "".join(keyStrokeContent)

inputByMilestone = splitByMilestone(keyStrokeContent)

for interval in inputByMilestone:
    print interval.split("\n")[0]
    print "# of CMD TAB COMBO: " + str(countCmdTabCombo(interval))
    print "# of CMD: " + str(countCmdNumber(interval))
    print "Average Typing Speed (key/second): " + str(calAverageTypingSpeed(interval)) 
    print "\n"
    
# # sample output
# ---5min KeyLogger milestone--- 2018-11-30-15:28:44
# # of CMD TAB COMBO: 0
# # of CMD: 8
# Average Typing Speed (key/second): 2.06


# ---5min KeyLogger milestone--- 2018-11-30-15:33:45
# # of CMD TAB COMBO: 1
# # of CMD: 8
# Average Typing Speed (key/second): 3.38


# ---5min KeyLogger milestone--- 2018-11-30-15:38:45
# # of CMD TAB COMBO: 0
# # of CMD: 20
# Average Typing Speed (key/second): 1.54