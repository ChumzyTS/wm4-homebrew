import json

fileDir = "C:\\Users\\hawki\\Documents\\Personal\\DnD\\wm4-homebrew\\Scripts\\input.txt"

data = {
    "name": "",
    "source": "WM4",
    "rarity": "",
    "entries": []
}

def process_tag_line(line):
    print("{0}: (Tag Line) {1}".format(lineNum, line))

def process_entry_line(line):
    print("{0}: (Description Line) {1}".format(lineNum, line))
    

with open(fileDir) as file:
    tagsDone = False
    for x in enumerate(file):
        # Line info
        lineNum = x[0]
        line = x[1].strip()
        
        if (lineNum == 0):
            # Title
            data["name"] = line
            
            print("{0}: (Title Line) {1}".format(lineNum, line))
        else:
            if not tagsDone:
                # Tag Line
                if (line == ""):
                    # End of tags
                    tagsDone = True
                    continue
                
                process_tag_line(line)
            else:
                process_entry_line(line)
    print()
    print(json.dumps(data, indent=4))
                
    