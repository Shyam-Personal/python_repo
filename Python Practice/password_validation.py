#password validation 
# one number, upeer case, special character, 8 length

import re

slist=["Sam@123", "shyam@123", "SHYAM@123", "Shyam@edr", "Shyam123", "ShYam@123"]

for s in slist:
	if len(s) < 8:
		print("Password is NOT valid1")
		continue
	if not re.search(r'[A-Z]', s):
		print("Password is NOT valid2")
		continue
	if not re.search(r'[a-z]', s):
		print("Password is NOT valid3")
		continue
	if not re.search(r'[0-9]', s):
		print("Password is NOT valid4")
		continue
	if not re.search(r'[_@$]', s):
		print("Password is NOT valid5")
		continue
	print("Password is valid")