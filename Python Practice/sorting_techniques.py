a = [64, 34, 25, 12, 22, 11, 90] 
n = len(a)

# Bubble Sort
for i in range(n):
	for j in range(n-i-1):
		if a[j] > a[j+1]:
			a[j], a[j+1] = a[j+1], a[j]	
print(a)

#=====================================
# Selection Sort

a = [64, 34, 25, 12, 22, 11, 90] 
n = len(a)

# Selection Sort
for i in range(n-1):
	for j in range(i+1, n):
		if a[i] > a[j]:
			a[i], a[j] = a[j], a[i]	
print(a)

#optimized selection sort
a = [64, 34, 25, 12, 22, 11, 90] 
n = len(a)

# Selection Sort
for i in range(n):
	min_ind = i
	for j in range(i+1, n):
		if a[min_ind] > a[j]:
			min_ind = j
	a[min_ind], a[i] = a[i], a[min_ind]	
print(a)