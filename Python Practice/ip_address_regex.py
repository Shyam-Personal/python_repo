#^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$

import re

if(re.match("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", input("Enter ip: "))):
	print("Valid IP")
else:
	print("Invalid IP")

	
# Example string  
s = 'Hello from shubhamg199630@gmail.com to priya@yahoo.com shy.am.desh_mukh1@gmail.co.in about the meeting @2PM'
  
# \S matches any non-whitespace character 
# @ for as in the Email 
# + for Repeats a character one or more times 
lst = re.findall('\S+@\S+', s)     
lst1 = re.findall(r'[\w._]+\@[\w._]+\.[\w._]+', s)  
# Printing of List 
print(lst)
print(lst1)