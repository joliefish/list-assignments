import csv

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
            writer.writerow(line)

