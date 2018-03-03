def yrange(n):
    for i in range(n,-1,-1):
        yield i
        
for x in yrange(5):
    print(x, end =" ")
print()
    
list1 = [1,2,3]
list2 = list1

list2[1] = 4
print(list1)
print(list2)