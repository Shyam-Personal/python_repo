#find the given key in the string

'''
a = "abdrkeabdkerykheyabdgtckehgkey"
sub = "key"

for i in range(len(a)):
    if a[i:i+3] == sub:
        print("Key is substring in string")
        break
else:
    print("Key is not substring in string")
'''
try:
    a = "abdrkeabdkerykheykeyabdgtckehketgkeysubjectkeyhfeygkey"
    sub = "key"
    cnt = 0
    sub_cnt = 0
    for i in a:
        if sub[cnt] == i:
            cnt += 1
            if cnt == len(sub):
                cnt = 0
                sub_cnt += 1
        else:
            cnt = 0
    print(sub_cnt)
    
except Exception as e:
    print(e,cnt)

a = "abdrkeabdkerykheykeyabdgtckehketgkeysubjectkeyhfeygkey"
sub = "key"
cnt = 0
n = 0

for _ in range(len(a)-len(sub)+1):
    if(sub == a[n:n+len(sub)]):
        cnt += 1
    n += 1
print("No of times {}".format(cnt))