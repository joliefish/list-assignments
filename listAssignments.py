# This is a program that receives a text input of a list of assignments from a syllabus
# and outputs a formatted list of assignments that can be pasted into Todoist

import dateutil.parser as dparser
from dateutil.parser import ParserError
import re

def convert(input, addons):
    output = ""

    # number of lines to combine
    combine = 1

    # open the given file in read mode
    # with open(input, 'r') as input:
    for line in input:
        # combine given number of lines
        for x in range(combine - 1):
            line = (line, next(input))
            line = '  '.join(line)

        # split line at multiple spaces, keyword 'due', or tab
        lineList = re.split('\\s{2,}|due|\\t', line.strip())

        # move time to beginning of list
        for x in range(len(lineList)):
            if re.search(r"\d[ap]m", lineList[x]):
                lineList.insert(0, lineList.pop(x).strip())
                lineList[0] = ' '.join((lineList[0], lineList.pop(1)))

        # prints date, time, and assignment name on the same line in that order
        dt = None
        for item in lineList:
            if dt == None:
                try:
                    dt, tokens = dparser.parse(item, fuzzy_with_tokens=True)
                    output += dt.strftime('%m-%d-%Y %H:%M') + ' '
                except ParserError:
                    pass
            else:
                # removes unwanted words
                output += item.replace('Assignment ','')

        output += ' ' + addons + '\n'

    return output
