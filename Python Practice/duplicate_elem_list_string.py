#Inplace remove duplicate elements from list
z=[1,2,1,2,3,2,1,3,3,2,1,2,1,2,1,2,3,4,3,4,3]

for i in z[:]:
	if z.count(i) > 1:
		z.remove(i)

print(z)

#Inplace remove duplicate characters of string
w="shdhssdhhsgdhsdhdsdhsdghsdgsdhsdgshdsgdsk"
for i in w[:]:
	cnt = w.count(i)
	if cnt > 1:
		w=w.replace(i,"",(cnt-1))
		
print(w)