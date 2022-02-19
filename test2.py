import pandas as pd

#header = ['date', 'name', 'time']

df = pd.read_csv("sample.txt",delimiter=' ')
df.to_csv('sampleOutput2.csv')

