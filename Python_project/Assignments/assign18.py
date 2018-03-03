'''
18. WaP to accept string from user and perform the below operation:
Ex:    Input: aabbbbbcccddaaaaa
    Output: a2b5c3d2a5
'''

a = "aabbbbbcccddaaaaa"
op = ""
cnt = 0

for i in range(len(a)-1):
    if a[i] == a[i+1]:
        cnt += 1        
    else:
        op = op + a[i] + str(cnt+1)
        cnt = 0 
op = op + a[i] + str(cnt+1)
print(op)