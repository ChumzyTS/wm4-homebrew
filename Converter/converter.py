import copy
import json
from enum import Enum

from line_parser import LineType
from reward import Reward

fileDir = "C:\\Users\\James\\Documents\\DnD\\wm4-homebrew\\Converter\\input.md"

END_REWARD_KEY = "---"

def getLineType(line, prevType):
    if (line == END_REWARD_KEY):
        return LineType.END_REWARD
    elif (prevType == LineType.END_REWARD):
        if (line == ""):
            return LineType.END_REWARD
        else:
            return LineType.NAME
    elif (prevType == LineType.NAME):
        return LineType.TAG
    elif (prevType == LineType.TAG):
        if (line == ""):
            return LineType.EMPTY
        elif ("prerequisite" in line):
            return LineType.PREREQ
        else:
            return LineType.COST_WEIGHT
    elif (prevType == LineType.COST_WEIGHT or prevType == LineType.PREREQ):
        return LineType.EMPTY
    elif (prevType == LineType.EMPTY or prevType == LineType.DESCRIPTION or prevType == LineType.LIST):
        if (line == ""):
            return LineType.EMPTY
        elif (line.find("* ") == 0):
            return LineType.LIST
        else:
            return LineType.DESCRIPTION
    
    return LineType.NIL


with open(fileDir) as file:
    prevLineType = LineType.END_REWARD
    rewards = []

    reward = Reward()
    rewards.append(reward)
    for x in enumerate(file):
        # Line info
        lineNum = x[0]
        line = x[1].strip()
        
        lineType = getLineType(line.lower(), prevLineType)

        if (lineType == LineType.END_REWARD):
            if (prevLineType != LineType.END_REWARD):
                reward = Reward()
                rewards.append(reward)
        else:
            reward.appendLine(line, lineType)
        
        prevLineType = lineType
    
    for reward in rewards:
        reward.generateData()
        print(reward)

        
                
    