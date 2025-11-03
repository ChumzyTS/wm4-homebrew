import os
import json
import time

# File Paths
scriptsFolder = os.path.dirname(os.path.abspath(__file__))
homebrewFolder = os.path.dirname(scriptsFolder)
componentsFolder = homebrewFolder + "\\Components\\"
outputFile = homebrewFolder + "\\wm4-homebrew.json"

# Get Component Data
parts = os.listdir(componentsFolder)
parts.sort()

data = {}
data["siteVersion"] = "2.7.4"
for part in parts:
    filePath = componentsFolder + part
    with open(filePath, 'r', encoding='utf8') as file:
        componentData = json.load(file)
        metaData = componentData["_meta"]
        name = metaData["name"]
        
        items = componentData["data"]
        if name in data:
            data[name] = data[name] + items
        else:
            data[name] = items

# Write Generated Metadata
data["_meta"]["dateLastModified"] = int(time.time())

# Write Compiled File
with open(outputFile, 'w', encoding='utf8') as file:
    json.dump(data, file, indent=4)
