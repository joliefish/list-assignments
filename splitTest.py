import re

# Split a string if multiple spaces

s = "hi hi  hi"
sArray = re.split('\\s{2,}', s)
print(sArray)
