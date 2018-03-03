list1 = []
for i in range(int(input())):
    list2 = [input(), eval(input())]
    list1.append(list2)    
print(list1)
    
lowest = list1[0]
sec_lowest = list1[-1]
list3 = []
for j in range(1,len(list1)):
    if (list1[j][1] < lowest[1]):
        print("in 1")
        list3=[]
        sec_lowest = lowest
        lowest = list1[j]
        list3.append(sec_lowest)
    elif(list1[j][1] < sec_lowest[1]):
        print("in 2")
        list3=[]
        sec_lowest = list1[j]
        list3.append(sec_lowest)
    elif (sec_lowest[1] == list1[j][1]):
        print("in 3")
        list3.append(list1[j])
print(lowest, sec_lowest)
print(list3)