import os
import json

# File Paths
scriptsFolder = os.path.dirname(os.path.abspath(__file__))
homebrewFolder = os.path.dirname(scriptsFolder)
componentsFolder = homebrewFolder + "\\Components\\"
outputFile = homebrewFolder + "\\wm4-homebrew.json"

# Combine
parts = os.listdir(componentsFolder)
parts.sort()

data = {}
data["siteVersion"] = "2.7.4"
for part in parts:
    filePath = componentsFolder + part
    with open(filePath, 'r', encoding='utf8') as file:
        name = part.removesuffix(".json")
        componentData = json.load(file)
        
        items = componentData[name]
        data[name] = items

with open(outputFile, 'w', encoding='utf8') as file:
    json.dump(data, file, indent=4)