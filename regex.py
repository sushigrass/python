import re


pattern = re.compile('match')

re.findall(pattern,'look for a match here this is a match look for anothethere') #returns list of matches

thestring = 'this is the string that i am going to try to match'
for i in re.finditer('th',thestring):
    locTuple = i.span()
    print locTuple #(0, 2) tuple of range index of matches
    print thestring[locTuple[0]:locTuple[1]]#actual string matched

all_matches = re.findall('\\b[abc]\\w*\\b','shoudl just return words that start with apple bacon cooking dude')
for word in all_matches:
    print word#apple bacon cooking

owlFood = 'cat rat bat sat'
regex = re.compile('[cr]at')
owlFood = regex.sub("owl",owlFood) #replaces cat and rat with owl
