#!/usr/bin/env python3

import urllib2
import re
import requests
import time

timeCounter = 240 * 24 #Used to send text at start of program
searchString = "CASCS411A(1|2)SoftwareENGDonham4.0Independent([1-9])+([0-9])*" #String to detect an open seat > 0


while True:
	obURL = "https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1448496759?ModuleName=univschr.pl&SearchOptionDesc=Class+Number&SearchOptionCd=S&KeySem=20174&ViewSem=Spring+2017&College=CAS&Dept=CS&Course=411&Section=" #URL leading to page containing section information
	html = str(urllib2.urlopen(obURL).read()) #HTML source code containing section information
	html = re.sub("\s","",html)
	html = re.sub("<[^>]*>","",html)
	html = re.sub("&[^;]*;","",html)
	html = re.sub("\\\\n","",html)  #Striped down version of page containing only text (whitespaced removed)
	# print(html)

	if bool(re.search(searchString, html)): #Checks if string is found
		r = requests.post("http://textbelt.com/text", data={'number': ----------, 'message': 'CS IS OPEN: https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1448498366?ModuleName=regsched.pl'}) #Uses textbelt api to send text with url to sign up (phone number omitted)
		print(r.status_code, r.reason) #Prints status code and response in case debugging is needed.
		print(r.text[:300] + '...')
		timeCounter = 0
		time.sleep(300) #Sleeps for 5 minutes to prevent repeated texting
	elif timeCounter < 240 * 24: #Increments time counter
		timeCounter = timeCounter + 1
	else: #Resets time counter and sends text once a day to inform me that program has not been terminated
		timeCounter = 0
		r = requests.post("http://textbelt.com/text", data={'number': ----------, 'message': 'CS is not open'})
		print(r.status_code, r.reason)
		print(r.text[:300] + '...')

	time.sleep(15) #Checks page every 15 seconds
