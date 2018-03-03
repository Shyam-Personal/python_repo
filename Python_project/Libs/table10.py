
for i in range (1,11):
    for j in range (1,11):
        print(i*j, end=" ")
    print("\n")
    
##################################
for i in range(1,11):
    print("%02d" %(i))
    
########################


def change1(x):
    x = 2000
    y=50
    return x,y

if __name__ == "__main__"  : 
    
    x = 1000
    a,b = change1(x=1000)
    print(a,b)


for x in "1234":
    print(x)