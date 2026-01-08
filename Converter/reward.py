import json
import line_parser

BASE_DATA = {
    "name": "",
    "source": "WM4",
    "rarity": "",
    "entries": [],
    "credit": []
}

class Reward:
    lines = []
    data = {}

    def __init__(self):
        self.data = BASE_DATA
        self.lines = []

    def appendLine(self, line, lineType):
        self.lines.append([lineType, line])
    
    def generateData(self):
        for line in self.lines:
            line_parser.parseLine(line[1], line[0], self.data)
        return self.data

    def __str__(self):
        return json.dumps(self.data, indent=4)