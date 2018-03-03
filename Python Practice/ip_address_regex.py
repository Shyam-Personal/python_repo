#^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$

import re

if(re.match("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", input("Enter ip: "))):
	print("Valid IP")
else:
	print("Invalid IP")
	
a = "shyam.deshmukh@gmail.com"
b = "shyam.deshmukh@gmail.com!"

if (re.match(r"^[\w._]+\@[\w._]+\.[\w._]+$", a)):
	print("Valid email " + a)
else:
	print("Invalid Email " + a)
	
if (re.match(r"^[\w._]+\@[\w._]+\.[\w._]+$", b)):
	print("Valid email " + b)
else:
	print("Invalid Email " + b)