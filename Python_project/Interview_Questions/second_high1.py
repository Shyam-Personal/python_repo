list1 = []
for i in range(int(input())):
    list2 = [input(), eval(input())]
    list1.append(list2)    
print(list1)
    
lowest = list1[0]
sec_lowest = list1[0]
dict1 = {}

for j in range(len(list1)):
    print(dict1)
    print("print b1 {} {}".format(list1[j][1],lowest[1]))
    if (list1[j][1] < lowest[1]):
        print("in 1")
        sec_lowest = lowest
        if sec_lowest[1] in dict1.keys():
            dict1[sec_lowest[1]].append(sec_lowest[0])
        else:
            dict1[sec_lowest[1]] = [sec_lowest[0]]
        lowest = list1[j]               
    elif(list1[j][1] < sec_lowest[1] and list1[j][1] > lowest[1]):
        print("in 2")
        sec_lowest = list1[j]
        if sec_lowest[1] in dict1.keys():
            dict1[sec_lowest[1]].append(sec_lowest[0])
        else:
            dict1[sec_lowest[1]] = [sec_lowest[0]]
    elif (sec_lowest[1] == list1[j][1]):
        print("in 3")
        if sec_lowest[1] in dict1.keys():
            dict1[sec_lowest[1]].append(list1[j][0])
        else:
            dict1[sec_lowest[1]] = [list1[j][0]]
    elif (lowest[1] == list1[j][1]):
        if lowest[1] in dict1.keys():
            dict1[lowest[1]].append(list1[j][0])
        else:
            dict1[lowest[1]] = [list1[j][0]]
        
print(lowest, sec_lowest)
print(dict1)
print(dict1[sec_lowest[1]])
