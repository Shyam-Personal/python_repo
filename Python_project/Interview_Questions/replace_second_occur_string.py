'''Remove the repeated character in string except the first occurrence & except the vowels.'''

import re
a = "abcarhshyashuydhsdhudhsyu"

print("original string: " + a)
for i in set(a):
    if i not in ['a','e','i','o','u']:
        if len(re.findall(i,a)) > 1:
            f = a[:int(a.index(i))+1]
            s = a[int(a.index(i))+1:]
            s = s.replace(str(i),"")
            a = f + s
print(a)

a = "abcarhshyashuydhsdhudhsyu"
for i in a[:]: 
	if i not in ['a','e','i','o','u']:
		cnt = a.count(i)
		if cnt > 1:
			a = a.replace(i, "", cnt-1)
print(a)

a = "abcarhshyashuydhsdhudhsyu"
for i in a[:]:
	if i not in ['a','e','i','o','u']:
		if a.count(i) > 1:
			ind = a.find(i)
			a = a[:ind+1] + a[ind+1:].replace(i,"")
print(a)