li = [3,2,4,5,1]
#li = [3,4,5,1,8,0,6,7,2]

le = len(li)
for i in range(0,le-1):
    #print(li[i])
    for j in range(i+1,le):
        if li[i] - li[j] == 2 or li[j] - li[i] == 2:
            print("("  + str(li[i]) + ',' + str(li[j]) + ")")