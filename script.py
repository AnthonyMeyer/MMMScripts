# Client side web script 
# Intellectual property of Anthony Meyer
# 9/27/14

# Imports
import re
from mechanize import Browser
import urllib2

# Pragma - Functions
def get_redirected_url(url):
	opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
	request = opener.open(url)
	return request.url

# Pragma - Dashboard login
print "Please enter the name of your webpage: "
domainName = raw_input()

domainName =  get_redirected_url(domainName + "/wp-admin")

dashBoard = Browser()
dashBoard.open(domainName)

print dashBoard.title()
dashBoard.select_form('loginform')
print "Username: "
userName = raw_input()
print "Password: "
password = raw_input()

dashBoard.form['log'] = userName
dashBoard.form['pwd'] = password

dashBoard.submit()
print dashBoard.title()

# Pragma - Uploading theme
