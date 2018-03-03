def isJumble(num):
    str_num = str(num)
    for i in range(len(str_num)-1):
        if(abs(int(str_num[i])-int(str_num[i+1])) != 1):
            return False
    else:
        return True
    
for i in range(1000):
    if(isJumble(i)):
        print(i, end=" ")