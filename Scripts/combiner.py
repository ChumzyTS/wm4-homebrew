import os
import json

# File Paths
homebrewFolder = "C:\\Users\\hawki\\Documents\\Personal\\DnD\\wm4-homebrew\\"
componentsFolder = homebrewFolder + "Components\\"
outputFile = homebrewFolder + "wm4-homebrew.json"

# Combine
parts = os.listdir(componentsFolder)
parts.sort()

data = {}
data["siteVersion"] = "2.7.4"
for part in parts:
    filePath = componentsFolder + part
    print(filePath)
    with open(filePath, 'r', encoding='utf8') as file:
        name = part.removesuffix(".json")
        componentData = json.load(file)
        
        items = componentData[name]
        data[name] = items
    

print(data)

with open(outputFile, 'w', encoding='utf8') as file:
    json.dump(data, file, indent=4)