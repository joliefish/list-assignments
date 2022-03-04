import csv
import datefinder

header = ['date', 'name', 'time']
#data = ['Afghanistan', 652090, 'AF']

# open the file in the write mode
with open('sample.txt', 'r') as input:

    with open('sampleOutput.csv', 'w') as output:
        # create the csv writer
        writer = csv.writer(output)

        # write header to the csv file
        writer.writerow(header)

        for line in input:
            # write a row to the csv file

            input_string = line
            # a generator will be returned by the datefinder module. I'm typecasting it to a list.
            # Please read the note of caution provided at the bottom.
            matches = list(datefinder.find_dates(input_string))
            date = matches[0]
            print(date)

            writer.writerow(line)

