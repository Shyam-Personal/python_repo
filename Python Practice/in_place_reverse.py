#Inplace reverse list
l=[1,2,3,4,5,6,7,8,9]
n = len(l)-1

for i in range(len(l)//2):
	l[i], l[n-i] = l[n-i], l[i]
print(l)

l=[1,2,3,4,5,6,7,8,9,10]
n = len(l)-1

for i in range(len(l)//2):
	l[i], l[n-i] = l[n-i], l[i]
print(l)

#Inplace reverse string
#i/p : "shyam deshmukh" o/p: 'mayhs hkumhsed'
w="shyam deshmukh"
w = " ".join([x[::-1] for x in w.split()])
print(w)

#i/p : "shyam deshmukh" o/p: 'hkumhsed mayhs'
w="shyam deshmukh"
w = "".join(reversed(w))
print(w)