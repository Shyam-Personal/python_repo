'''Remove the repeated character in string except the first occurrence & except the vowels.'''

import re
a = "abcarhshyashuydhsdhudhsyu"

for i in set(a):
    if i not in ['a','e','i','o','u']:
        if len(re.findall(i,a)) > 1:
            f = a[:int(a.index(i))+1]
            s = a[int(a.index(i))+1:]
            s = s.replace(str(i),"")
            a = f + s
print(a)