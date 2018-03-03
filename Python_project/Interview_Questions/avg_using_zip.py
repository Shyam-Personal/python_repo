import functools

stu, sub = input().split(" ")
stu, sub = [int(stu), int(sub)]
list1 = []
for i in range(int(sub)):
    list2=[]
    list2 = input().split(" ")
    list2 = [float(x) for x in list2]
    list1.append(list2)
    
for j in zip(*list1):
    sum1 = functools.reduce(lambda x,y : x+y, j)
    avg = sum1 / sub
    print(avg)