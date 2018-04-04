import re


pattern = re.compile('match')

re.findall(pattern,'look for a match here this is a match look for anothethere') #returns list of matches

#finditer
thestring = 'this is the string that i am going to try to match'
for i in re.finditer('th',thestring):
    locTuple = i.span()
    print locTuple #(0, 2) tuple of range index of matches
    print thestring[locTuple[0]:locTuple[1]]#actual string matched

#findall
all_matches = re.findall('\\b[abc]\\w*\\b','shoudl just return words that start with apple bacon cooking dude')
for word in all_matches:
    print word#apple bacon cooking

#substitution
owlFood = 'cat rat bat sat'
regex = re.compile('[cr]at')
owlFood = regex.sub("owl",owlFood) #replaces cat and rat with owl

#rawstring raw string
randomstring = 'this is \\stuff'
re.search(r'\\stuff',randomstring)

randstr = 'C.S.E. C.S.I.S. N.S.A. C.I.A.'
print len(re.findall('.\..\..\.',randstr))
#anything dot anything dot anything dot

randstr2 = '''this is a long
string that goes on
for a few lines
ahhahhahahahah
ok
'''

regex = re.compile('\n')
nolines = regex.sub(" ",randstr2)

numstr = '123 1234 12344 123456 1234567'
print len(re.findall("\\b\d{5}\\b",numstr))
#5 digit number words

pnum = '123-123-1234'
if re.search('\w{3}-\w{3}-\w{4}',pnum):
    print "its legit"

email = re.compile('[\w._%+-]{1,20}@[\w.-]{2,20}\.[A-Za-z]{2,3}')
