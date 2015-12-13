#!/usr/bin/env python

import urllib2
import smtplib
import time

fromaddr = 'astrodreamer18@gmail.com'
toaddrs  = 'astrodreamer18@gmail.com'
# Credentials (if needed)
username = 'astrodreamer18'
password = ''

# The actual mail send
time_counter = 0;
# count the time just to send the email every 3 hours
while(True):
	try:
	
		if (time_counter == 10800):
			time_counter =0;
		
		if(time_counter==0):	
			#get public IP
			myip = urllib2.urlopen("http://myip.dnsdynamic.org/").read()
			myip = "the public IP of PSSP is "+myip
			msg = "\r\n".join(["From: astrodreamer18@gmail.com","To: astrodreamer18@gmail.com",  "Subject: Public IP","",  myip ])
			#send IP over Email
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.starttls()
			server.login(username,password)
			server.sendmail(fromaddr, toaddrs, msg)
			server.quit()
			print 'successfully sent the mail'
		else:
			print 'waiting for the next ' + str((10800- time_counter)) + ' seconds'	
		time.sleep(1)# sleep for one second
		time_counter = time_counter +1
	except:
		print 'failed to send mail'