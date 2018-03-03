def Square(no):
    return no*no

import functools
for i in map(Square, range(1,11)):
    print(i,end=" ")
    
def IsMultiplyOf5(no):
    return no%5 == 0
print("")
for j in filter(IsMultiplyOf5, range(1,101)):
    print(j,end=" ")
    
def multiply(x,y):
    return x*y
print("")
print(functools.reduce(multiply, range(1,5)))