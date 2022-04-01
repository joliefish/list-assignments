import pandas as pd

#header = ['date', 'name', 'time']

df = pd.read_csv("sampleTest.txt", delimiter= ' ')
df.to_csv('sampleTestOutput1.csv')

