import math 
'''
for i in range(int(input())):
    n = int(input())
    
    if (n > 2):
        if (n % 2 == 0):
            print("Not prime")
        else:
            for j in range(3, int(math.sqrt(n))+1):
                if(n % j == 0):
                    print("Not prime")
                    break
            else:
                print("Prime")
				
    else:
        if n == 2:
            print("Prime")
        else:
            print("Not prime")
'''
for n in range(3, 100):
	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0 or n < 3:
			break
	else:
		print("{} Prime".format(n))