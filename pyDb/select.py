#!/usr/bin/python

import MySQLdb

f = open('../../.hello.txt','r')
pw = f.read()
passw = pw.strip()
f.close()
# Open database connection
db = MySQLdb.connect("localhost","root",passw,"petergillis")
print db
# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEES \
       WHERE Id> '%d'" % (0)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      _id = row[0]
      age = row[1]
      first = row[2]
      last = row[3]
      # Now print fetched result
      print "fname=%s,lname=%s,age=%d,id=%d" % \
             (first, last, age, _id)
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
