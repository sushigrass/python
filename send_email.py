
#smtp
import smtplib
fromaddr="petergillis707@gmail.com"
toaddr="simonscape1234@gmail.com"
message="fuk u"
password=""
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr,password)
for x in xrange(500):
    server.sendmail(fromaddr,toaddr,message)
    print "sent: ",x
server.quit()
