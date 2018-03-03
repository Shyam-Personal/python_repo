def Increement(n):
    return lambda x: x+n

x = Increement(5)
print(x(1))
print(x(1))

y = Increement(10)

#===========================================
#Next example

fd = open("occur.txt")
lines = fd.readlines()

iter1 = map(lambda x : len(x), lines)

for i in iter1:
    print(i,end=" ")

fd.close()