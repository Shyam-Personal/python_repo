import math

def main():
    n = int(input("Enter the no: "))
    sr = int(math.sqrt(n))
    flag = 1
    
    for i in range(2,sr):
        if not n%i:
            print("Given no {} is NOT Prime Number".format(n))
            flag=0
            break
    
    if flag == 1:    
        print("Given no {} is Prime Number".format(n))            

if __name__ == "__main__":
    main()