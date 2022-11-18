# This is a program that receives a text input of a list of assignments from a syllabus
# and outputs a formatted list of assignments that can be pasted into Todoist

import dateutil.parser as dparser
from dateutil.parser import ParserError
import re
import pandas as pd

def convert(input, addons):
    """
    input - list of assignments (each line with assignment name and due date)
    addons - str, to add to each assignment
    """
    sections = ['date', 'name', 'time']
    unwanted = ['Assignment']
    df = pd.DataFrame()

    # Lines are rows in the DataFrame
    for line in input:
        # Split line at multiple spaces, keyword 'due', or tab
        line_list = re.split('\\s{2,}|due|\\t', line.strip()) 
        line_list = [x for x in line_list if x != '']       
        next_row = pd.DataFrame([line_list])
        # Adds the row to the DataFrame
        df = pd.concat([df, next_row])
    
    # Renames the columns from indices to sections
    rename = {key : value for key, value in enumerate(sections)}
    df = df.rename(columns=rename)

    # Creates column with datetime
    df['datetime_str'] = df['date'] + df['time']
    df['datetime'] = df['datetime_str'].apply(dparser.parse, fuzzy_with_tokens=True).str[0]
    #             output += dt.strftime('%m-%d-%Y %H:%M') + ' '

    # Removes unwanted words from assignment name
    for word in unwanted:
        print(word)
        df['name'] = df['name'].str.replace(word, '').str.strip()

    df['output'] = df['datetime'].apply(lambda x: x.strftime('%m-%d-%Y %H:%M')) + ' ' + df['name']
    print(df)

    return df['output'].tolist()

with open('test_homeworks\info200hw.txt') as f:
    print(convert(f.readlines(), ''))