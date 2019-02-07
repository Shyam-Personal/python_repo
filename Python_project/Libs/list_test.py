list1 = [2,1,2,3,1,3,9,12,2,3,4,100,3,4,5,24,3,2,1]
for item in list1[:]:
    if item < 5 :
        list1.remove(item)

print(list1) 