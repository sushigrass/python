import re


names = ['petergillis','jongillis']

pattern = re.compile('petergillis')
matches = pattern.findall(names)

for match in matches:
    print match
