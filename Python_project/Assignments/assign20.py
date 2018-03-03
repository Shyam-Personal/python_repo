'''
20. WaP to accept string from user, accept also a character and perform the below operation on that string
Ex:    Input: babble
    Output: ba**le
'''

a = "babble"
char = 'b'

for i in range(len(a)):
    if a[i] == char:
        index = i
        break
first = a[0:index+1] 
second = a[index+1:].replace(char,"*")
print(first + second)

a = "areubuntibubbly"
print(a[:a.find(char)+1] + a[a.find(char)+1:].replace(char, "*"))