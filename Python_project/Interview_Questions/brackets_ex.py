'''
st = "(())))(())("
open11 = 0
close = 0
dict_open = {}
dict_close = {}
cnt = 0
for i in st:
    cnt += 1
    if i == "(":
        open11 += 1
        dict_open[open11] = cnt
        
    if i == ")":
        close += 1
        dict_close[close] = cnt
    
print(open11,close)
print(dict_open, dict_close)
'''
st = "()()()()()()(((((()"
#st = "(())))((())()"
arr =[]
i = 0
open1 = 0
close1 = 0
j = len(st)-1
while(i < len(st)):
    if(st[i] == "("):
        open1 += 1
    
    if st[j] == ")":
        close1 += 1
        
    if open1 == close1:
        arr.append(i)
        if i > j:
            print(i,j)
            break
    i += 1
    j -= 1
print(open1,close1,arr)