import re

pattern = re.compile('match')

re.findall(pattern,'look for a match here this is a match look for anothethere') #returns list of matches
