'''
#1
li = [1,2,3,4,5]
li1 = [i+1 for i in li]
print(li1)
'''
#2
X=Y=Z=1
N=2

li2 = [1,2,3,4,5]

li3 = [n*n for n in li2]

print(li3)

import os
print(dir(os))


def yrange():
    li5 = range(5)
    for i in li5[::-1]:
        yield i

test = yrange()

for l in test:
    print(l)