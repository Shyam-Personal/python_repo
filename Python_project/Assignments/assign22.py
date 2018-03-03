'''
22. Write list comprehension to generate the following list:
a. List of squares within given range
b. List of cubes in given range
c. List of Even numbers in given range
d. List of Odd numbers in given range, also compute the squares of that Odd numbers using List comprehension
e. List of multiples of 5 in given range
f. List of Tables in given range
g. List of intersection of 2 given lists
h. List of Special numbers
i. List of unique elements
'''

print([x**2 for x in range(6)])
print([x**3 for x in range(6)])
print([x for x in range(11) if not x%2])
print([x for x in range(11) if x%2])
print([x**2 for x in range(11) if x%2])
print([x for x in range(101) if not x%5])
print([x*y for y in range(1,5) for x in range(1,11)])
print([x for x in [i for i in range(11)] for y in [4,7,11,14] if x == y])
#print special num
print([x for x in [i for i in range(11)] if x not in [4,7,11,1]])