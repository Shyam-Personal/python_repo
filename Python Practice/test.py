'''
for i in range(1,5): #More than 2 lines will result in 0 score. Do not leave a blank line also
    while i > 0: print(i,end=""); i-=1 else: pass
''

n = eval(input())

print([n for n in map(lambda x,y : x+y,[i for i in range(n)],[j for j in range(n)])])

''

def fibo1(n):
	fibo = []
	for i in range(n):
		if i == 0:
			fibo.append(0)
		elif i == 1:
			fibo.append(1)
		else:
			fibo.append(fibo[i-1] + fibo[i-2])
	return fibo

print([x**3 for x in fibo1(5)])



z = input()

n,m = z.split(" ")

print(n,m)
''

z = input()
n,m = z.split(" ")
li = []
for i in range(int(n)):
    li.append(input())

k = []
dict1 = {}
for j in range(int(m)):
    k = input()
    arr1 = [str(int(q)+1) for q in range(len(li)) if li[q] == k]
    dict1[k] = arr1
    print(" ".join(arr1))
''

def decorate_number(num):
    def wrapper(num):
        if len(num) == 11:
            num = num.replace("0","",1)
        elif len(num) == 12:
            num = num.replace("91","",1)
        elif len(num) == 13:
            num = num.replace("+91","",1)
        num1 = "+91 " + num[:5] + " " + num[5:]
        return num1
    return wrapper
    
@decorate_number
def print_num(num):
    return num

def main():
    n = input()
    li = []
    for i in range(int(n)):
        li.append(print_num(input()))
    li.sort()
    
		
main()

for x in sorted(['+91 {0}{1}{2}{3}{4} {5}{6}{7}{8}{9}'.format(input()[-10:]) for _ in range(input())]):print(x)
''
import urllib.request
with urllib.request.urlopen('https://sma-stg.stellus.com/downloads') as f:
	print(f.read(300))
''

import urllib3
response = urllib3.urlopen('http://python.org/')
html = response.read()
print(html)
''

import requests
url = 'https://updates.opendns.com/nic/update?hostname='
username = 'username'
password = 'password'
print(requests.get(url, auth=('shyam.d@stellus.com', 'stellus1!')).content)
''

#!/bin/python3

import sys
import functools

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
    
n = len(arr[0])-2
m = len(arr)-2
flag = 1
for i in range(m):
    for j in range(n):
        sum1 = functools.reduce(lambda x,y:x+y, [arr[i][j],arr[i][j+1],arr[i][j+2],arr[i+1][j+1],arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]])
        if j == 0 and flag == 1:
            max1 = sum1
            flag = 0
            continue
        if max1 < sum1:
            max1 = sum1
print(max1)
'''

#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    
    max_pos = 0
    flag = 0
    for i in range(1, n):
        print("in i")
        for j in range(i+1, n+1):
            print("in j")
            if (i&j > max_pos and i&j < k):
                max_pos = i&j  
                if max_pos == k-1:
                   flag = 1
                   print("break condition")
                   break
        if flag:
           break
    print(max_pos)