import os
import json
from operator import itemgetter

# File Paths
scriptsFolder = os.path.dirname(os.path.abspath(__file__))
homebrewFolder = os.path.dirname(scriptsFolder)
componentsFolder = homebrewFolder + "\\Components\\"

# 
def itemSort(item, sortData):
    sortInfo = []

    for sort in sortData:
        sortType = sort["type"]
        sortKey = sort["key"]

        if (sortType == "a-z"):
            sortInfo.append(item[sortKey])
        if (sortType == "custom"):
            sortOrder = sort["order"]
            sortInfo.append(sortOrder.get(item[sortKey], float('inf')))

    return sortInfo

# Combine
parts = os.listdir(componentsFolder)
parts.sort()

for part in parts:
    filePath = componentsFolder + part
    componentData = {}
    with open(filePath, 'r', encoding='utf8') as file:
        name = part.removesuffix(".json")
        componentData = json.load(file)
        
        items = componentData[name]
        if "sort" in componentData:
            sortData = componentData["sort"]

            items = sorted(items, key=(lambda item: itemSort(item, sortData)))

        componentData[name] = items
    
    with open(filePath, 'w', encoding='utf8') as file:
        json.dump(componentData, file, indent=4)

    

print("")