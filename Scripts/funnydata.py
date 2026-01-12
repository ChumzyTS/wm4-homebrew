import os
import json

# File Paths
scriptsFolder = os.path.dirname(os.path.abspath(__file__))
homebrewFolder = os.path.dirname(scriptsFolder)
outputFile = homebrewFolder + "\\wm4-homebrew.json"

credits = {

}

with open(outputFile, 'r', encoding='utf8') as file:
    data = json.load(file)
    for key in data:
        dataType = data[key]
        for i in dataType:
            if "credit" in i:
                gms = i["credit"]["gms"]
                if gms:
                    for gm in gms:
                        gm = gm.strip()
                        if gm in credits:
                            credits[gm] += 1
                        else:
                            credits[gm] = 1

print("")
for gm in dict(sorted(credits.items(), key=lambda item: -item[1])):
    print("{0}: {1}".format(gm, credits[gm]))