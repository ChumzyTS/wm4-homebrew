from enum import Enum
import os
import json

# Line Type
class LineType(Enum):
    NIL = 0
    NAME = 1
    TAG = 2      
    COST_WEIGHT = 3
    PREREQ = 4
    DESCRIPTION = 5
    CREDIT = 6
    SKIP = 7
    EMPTY = 8
    LIST = 9
    END_REWARD = 100

# Load Data
DATA_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "\\data\\"

def loadJson(name):
    fileName = DATA_FOLDER + name + ".json"
    with open(fileName, 'r', encoding='utf8') as json_data:
        d = json.load(json_data)
        json_data.close()
        return d[name]

rarities = loadJson("rarities")
types = loadJson("types")
tags = loadJson("tags")
currencies = loadJson("currencies")
categories = loadJson("categories")

# Get Line Info
def getAttunement(line):
    line = line.lower()
    reqAttnStr = "requires attunement"
    if (reqAttnStr in line):
        attnInfoIdx = line.find(reqAttnStr) + len(reqAttnStr)
        attnInfo = line[attnInfoIdx:]
        endAttnInfoIdx = attnInfo.find(")")
        if (endAttnInfoIdx == 0):
            return True
        else:
            attnInfo = attnInfo[1:endAttnInfoIdx]
            return attnInfo
    return False

def getCategory(line):
    line = line.lower()
    for category in categories.keys():
        if (category in line):
            return categories[category]
    return "none"

def getCost(line):
    line = line.lower()
    for currency in currencies.keys():
        if (currency in line):
            endCost = line.find(currency) - 1
            cost = int(line[:endCost])
            cost = cost * currencies[currency]
            return cost
    return 0

def getRarity(line):
    line = line.lower()
    for rarity in rarities:
        if (rarity in line):
            return rarity
    return "none"

def getTags(line):
    line = line.lower()
    lineTags = []
    for tag in tags.keys():
        if (tag in line):
            lineTags.append(tags[tag])
    return lineTags

def getType(line):
    line = line.lower()
    for type in types:
        if (type in line):
            return type
    return "item"

def getWeight(line):
    line = line.lower()
    if ("lb" in line):
        # Has Listed Weight
        endWeight = line.find("lb") - 1
        startWeight = 0
        if (line.find(",") != -1):
            startWeight = line.find(",") + 2
        weight = line[startWeight:endWeight]
        if ("/" in weight):
            # Fractional Weight
            weightParts = weight.split("/")
            weightNum = float(weightParts[0])
            weightDen = float(weightParts[1])
            return float(weightNum / weightDen)
        return int(weight)
    # No Listed Weight
    return 0

def convertFormat(line):
    # Bold
    boldOpen = False
    while (line.find("**") != -1):
        if (not boldOpen):
            line = line.replace("**", "{@b ", 1)
        else:
            line = line.replace("**", "}", 1)
        boldOpen = not boldOpen

    # Italic
    italicOpen = False
    while (line.find("*") != -1):
        if (not italicOpen):
            line = line.replace("*", "{@i ", 1)
        else:
            line = line.replace("*", "}", 1)
        italicOpen = not italicOpen
    
    return line

# Formatting
def parseLine(line, lineType, data):
    if lineType == LineType.NIL:
        # Error has occured
        return data
    elif lineType == LineType.NAME:
        line = line.replace("*", "")
        data["name"] = line
    elif lineType == LineType.TAG:
        # Get Type
        type = getType(line)

        if (type == "item"):
            category = getCategory(line)
            if (category != "none"):
                data["type"] = category
            else:
                data["wondrous"] = True
        else:
            data["type"] = type.capitalize()
        
        if (type == "item" or type == "talent"):
            attunement = getAttunement(line)
            data["reqAttune"] = attunement
        
        rewardTags = getTags(line)
        if (len(rewardTags) != 0):
            data["property"] = rewardTags

        # Set Rarity
        rarity = getRarity(line)
        data["rarity"] = rarity
    elif lineType == LineType.COST_WEIGHT:
        line = line.replace("*", "")

        # Get Cost
        cost = getCost(line)
        if (cost != 0):
            data["value"] = cost

        # Get Weight
        weight = getWeight(line)
        if (weight != 0):
            data["weight"] = weight
    elif lineType == LineType.PREREQ:
        line = line.replace("*", "")
        
        data["entries"].append("{@i " + line + "}")
    elif lineType == LineType.DESCRIPTION:
        line = convertFormat(line)

        data["entries"].append(line)
    elif lineType == LineType.LIST:
        line = line[2:]
        line = convertFormat(line)

        
        data["entries"].append(
                {
                    "type": "list",
                    "items": [
                        line
                    ]
                }
            )
        
    return data
