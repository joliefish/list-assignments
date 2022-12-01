# This is a program that receives a text input of a list of assignments from a syllabus
# and outputs a formatted list of assignments that can be pasted into Todoist

import dateutil.parser as dparser
from dateutil.parser import ParserError
import re
import pandas as pd

def convert(input, addons):
    """
    Converts a list of assignments to a Todoist-friendly format
    input - list of assignments (each line with assignment name and due date)
    addons - str, to add to each assignment
    """

    df = parseInput(input)

    # Renames the columns of df from indices to sections
    # Note: UI function - modify sections
    sections = ['date', 'name', 'time']
    rename = {key : value for key, value in enumerate(sections)}
    df = df.rename(columns=rename)

    # Creates column with datetime
    df['dt_temp'] = df['date'] + df['time']
    df['dt'] = df['dt_temp'].apply(dparser.parse, fuzzy_with_tokens=True).str[0]

    # Note: UI function - modify unwanted
    unwanted = ['Assignment']
    removeUnwanted(df, unwanted)

    # Creates column with correctly formatted task
    df['output'] = df['dt'].apply(lambda x: x.strftime('%m-%d-%Y %H:%M')) + \
                   ' ' + df['name']

    return df['output'].tolist()


def parseInput(input):
    """
    Returns a parsed DataFrame of tasks based on multiple spaces, the keyword
    'due', or a tab
    input - list of assignments
    """
    df = pd.DataFrame()
    # Note: Lines are rows in the DataFrame
    for line in input:
        # Split line at multiple spaces, keyword 'due', or tab
        line_list = re.split('\\s{2,}|due|\\t', line.strip())
        # Removes empty splits
        line_list = [x for x in line_list if x != '']
        # Adds the row to the DataFrame
        next_row = pd.DataFrame([line_list])
        df = pd.concat([df, next_row])
    return df


def removeUnwanted(df, unwanted):
    """
    Removes unwanted words from assignment names
    df - DataFrame of tasks
    unwanted - list of unwanted words
    """
    for word in unwanted:
        df['name'] = df['name'].str.replace(word, '').str.strip()


with open('test_homeworks\info200hw.txt') as f:
    print(convert(f.readlines(), ''))