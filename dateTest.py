# import datefinder

# input_string = "3 February 2022"
# # a generator will be returned by the datefinder module. I'm typecasting it to a list. Please read the note of caution provided at the bottom.
# matches = list(datefinder.find_dates(input_string))

# date = matches[0]
# print(date)

import csv
import dateutil.parser as dparser
from dateutil.parser import ParserError
import re

header = ['date', 'name', 'time']
combine = 1

# open the file in the write mode
with open('info200hw.txt', 'r') as input:

    #with open('sampleOutput.csv', 'w') as output:
        # create the csv writer
        #writer = csv.writer(output)

        # write header to the csv file
        #writer.writerow(header)

        # prints datetime, extraneous information on separate lines
    for line in input:
        # combine given number of lines
        for x in range(combine - 1):
            line = (line, next(input))
            line = '  '.join(line)            

        # split line at multiple spaces, keyword 'due'
        lineList = re.split('\\s{2,}|due|\\t', line.strip())

        for x in range(len(lineList)):
            try:
                # move time to beginning of tuple
                if 'am' in lineList[x] or 'pm' in lineList[x]:
                    lineList.insert(0, lineList.pop(x).strip())
                    lineList[0] = ' '.join((lineList[0], lineList.pop(1)))
            except IndexError:
                print("ERROR, NEXT")

        # None same as null
        dt = None
        for item in lineList:
            if dt == None:
                try:
                    dt, tokens = dparser.parse(item, fuzzy_with_tokens=True)
                    print(dt.strftime('%m-%d-%Y %H:%M'), end = ' ')
                except ParserError:
                    pass
            else:
                print(item.replace('Assignment ',''), end = '')

        print('')

            # # write a row to the csv file
            # dt, tokens = dparser.parse(line, fuzzy_with_tokens=True)
            # print(tokens)
            # print(dt)