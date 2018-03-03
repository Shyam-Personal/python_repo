'''
13. WaP to print Fibonacci series upto n (n - Accept from user)
'''

def fibbonacci(num):
    fib = [] 
   
    for i in range(num):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[i-1] + fib[i-2])
    return fib    

def main():
    num = int(input("Enter the number : "))
    print(fibbonacci(num))

if __name__=="__main__":
    main()