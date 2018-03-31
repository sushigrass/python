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

# Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEES WHERE AGE > '%d'" % (200)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
