#testing stuff number^2 up to n python 3
[print(i**2) for i in range(n)]

#leap year
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

#print 1 to n separated by spaces
print(*range(1, int(input())+1), sep='')


#reverse a string
name = "peter gillis"
backwards = ""
for i in xrange(len(name),0,-1):
    backw += name[i-1]
#multiplying fractions
import operator
def product(fracs):
    t =  reduce(operator.mul , fracs)
    return t.numerator, t.denominator
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

#list to string and change 1 character
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)

#count occurnces of substring in a string
def count_substring(string, sub_string):
    counter = 0
    sub_len = len(sub_string)
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:(i + sub_len)] == sub_string:
                counter = counter + 1
    return counter

#converted this to list comprehension
def count_substring(string, sub_string):
    return sum([1 if string[i] == sub_string[0] and string[i:(i+ len(sub_string))] ==
    sub_string else 0 for i in range(len(string))])
    #wrapped line for readability

#take string commands and perform eval on them
if __name__ == '__main__':
    n = input()
    l = []
    for i in range(int(n)):
        x = input()
        if x=='print':
            print(l)
        else:
            y = x.split()
            if len(y)==3:
                eval("l."+y[0]+'('+y[1]+','+y[2]+')')
            elif len(y)==2:
                eval("l."+y[0]+'('+y[1]+')')
            elif len(y)==1:
                eval("l."+y[0]+"()")

#convert string input to list of ints, then to tuple, then print hash(tuple)
if __name__ == '__main__':
    n = int(input())
    input_list = input().split()
    input_list = [int(x) for x in input_list]
    t = tuple(input_list)
    print(hash(t))

#find 2nd largest unique number (conver to set to remove dupes, sort, then [-2])
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print sorted(list(set(arr)))[-2]

#find all occurances of 2nd lowest score in list of names,grade
if __name__ == '__main__':
    marksheet = []
    for _ in range(0,int(input())):
        marksheet.append([input(), float(input())])

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

#find avg mark of queried studient to 2 decimal places python2 (reduce)
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    print('%2.2f'%(reduce(lambda x,y: x+y, student_marks[query_name])/len(student_marks[query_name])))

#more simply
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print('%2.2f'%(sum(student_marks[query_name])/len(student_marks[query_name])))

#regex
import re
for _ in range(int(input())):
    s = input()
    print('Valid' if all([re.search(r, s) for r in
    [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']])
    and not re.search(r'.*(.).*\1', s) else 'Invalid')
    #wrapped lined for readability

#Nested for loops:
if __name__ == '__main__':
    x, y, z, n = (int(input()) for _ in range(4))
    l = []
    for a in range(0,x+1):
        for b in range(0,y+1):
            for c in range(0,z+1):
                if a+b+c!=n:
                    l.append([a,b,c])
    print(l)
#same thing with list comprehension
if __name__ == '__main__':
    x, y, z, n = (int(input()) for _ in range(4))
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

#convert upper to lower and leave the rest alone
#for loop method:
def swap_case(s):
    l = list(s)
    for (i,char) in enumerate(l):
        if l[i].isalpha:
            if l[i].isupper():
                l[i] = l[i].lower()
            elif s[i].islower():
                l[i] = l[i].upper()
    return ''.join(l)
#much easier built in:
def swap_case(s):
    return s.swapcase()

#split string by space, then join by hyphen -
def split_and_join(line):
    return '-'.join(line.split())

#simple print
def print_full_name(a, b):
    print("Hello "+a+" "+b+"! You just delved into python.")

#check if string contains various types of chars
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

#sum and average of distinct items in a list (set)
def average(array):
    x = set(array)
    return sum(x)/len(x)

#symmetric_difference symmetric difference two sets
#print all items in list
m = int(input())
s1=set(map(int, ((input().split()))))
n = int(input())
s2=set(map(int, ((input().split()))))
print(*sorted(list(s1.symmetric_difference(s2))),sep="\n")

#check if sets contain numbers in array and increment value list comprehension
n,m = input().split()
arr = input().split()
a = set(input().split())
b = set(input().split())
happiness = [1 if x in a else -1 if x in b else 0 for x in arr]
print(sum(happiness))

#count unique items in set
n = int(input())
s = set()
for _ in range(n):
    s.add(input())
print(len(s))

#union of two sets (elements in either set, join in SQL)
n = int(input())
ln = set(input().split())
b = int(input())
lb = set(input().split())
print(len(ln.union(lb)))

#intersction (elements in both sets, inner join in SQL)
n = int(input())
ln = set(input().split())
b = int(input())
lb = set(input().split())
print(len(ln.intersection(lb)))

#difference (left join in SQL)
n = int(input())
ln = set(input().split())
b = int(input())
lb = set(input().split())
print(len(ln.difference(lb)))

#symmetric difference (opposite of inner join in SQL)
n = int(input())
ln = set(input().split())
b = int(input())
lb = set(input().split())
print(len(ln.symmetric_difference(lb)))
