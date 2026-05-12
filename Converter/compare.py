import os
import difflib

convertFolder = os.path.dirname(os.path.abspath(__file__))
homebrewFolder = os.path.dirname(convertFolder)
comparisonFolder = convertFolder + "\\comparison"
old_filepath = comparisonFolder  + "\\old.md\\"
new_filepath = comparisonFolder  + "\\new.md\\"
additions_filepath = comparisonFolder  + "\\additions.md\\"
removals_filepath = comparisonFolder  + "\\removals.md\\"

old_file = open(old_filepath, 'r', encoding='utf8')
new_file = open(new_filepath, 'r', encoding='utf8')

diff = difflib.ndiff(old_file.readlines(), new_file.readlines())
additions = ''.join(x[2:] for x in diff if x.startswith('+ '))
removals = ''.join(x[2:] for x in diff if x.startswith('- '))

with open(additions_filepath, 'w', encoding='utf8') as output:
    output.write(additions)
with open(removals_filepath, 'w', encoding='utf8') as output:
    output.write(removals)
