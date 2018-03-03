'''
Suppose 1 list is given [3,2,4,5,1] Output should
print the tuple of two numbers which has the
difference of 2. Expected output : (2,4) (3,5) (3,1)
'''

x = [3,2,4,5,1]

for i in range(len(x)):
    for j in range(i+1,len(x)):
        #if(x[j]-x[i] == 2 or x[i]-x[j] == 2):
        if(x[j]-x[i] in [-2,2]):
            print(tuple([x[i],x[j]]))