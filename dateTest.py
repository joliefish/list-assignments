# import datefinder

# input_string = "3 February 2022"
# # a generator will be returned by the datefinder module. I'm typecasting it to a list. Please read the note of caution provided at the bottom.
# matches = list(datefinder.find_dates(input_string))

# date = matches[0]
# print(date)

import csv
import dateutil.parser as dparser

header = ['date', 'name', 'time']

# open the file in the write mode
with open('sample.txt', 'r') as input:

    with open('sampleOutput.csv', 'w') as output:
        # create the csv writer
        writer = csv.writer(output)

        # write header to the csv file
        writer.writerow(header)

        for line in input:
            # write a row to the csv file
            dt, tokens = dparser.parse(line, fuzzy_with_tokens=True)
            print(tokens)
            print(dt)