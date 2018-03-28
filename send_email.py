#smtp
import smtplib
fromaddr="petergillis707@gmail.com"
toaddr="petergillis11@gmail.com"
message="helooooo"
password=""
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr,password)
for x in xrange(50):
    server.sendmail(fromaddr,toaddr,message)
    print "sent: ",x
server.quit()
