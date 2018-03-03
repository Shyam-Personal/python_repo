import math

def IsPrime(num):
    retVal = False
    if num > 1:
        if num & 1:
            for divisor in range(3,int(math.sqrt(num)+1),2):
                if num % divisor == 0:
                    break
            else:
                retVal = True
    return retVal     

def GetPrimes(n):
    for i in n:
        if IsPrime(i):
            yield i

def main():
    n = range(1,100)
    obj = GetPrimes(n) 
    
    #print(next(obj))
    for y in obj:
        print(y, end=" ")

if __name__ == "__main__":
    main()