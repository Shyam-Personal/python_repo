'''
##1. Write a program to accept number from user and check if the number is even
while(1):
    num = int(input("Enter the number to check even/odd or enter any other char to exit : "))
    print("Given number is even.") if (num%2 == 0) else print("Given no is Odd.")
    
    print("Given number is even.") if not (num & 1) else print("Given no is Odd.")
      
##2. WaP to accept number from user and accept bit position to turn OFF in given number
num = int(input("Enter the number : "))
pos = int(input("Enter the bit position : "))

print((num & ~(1 << (pos-1))))

#9. WaP to turn off right most one bit in a number
num = int(input("Enter the number : "))
print(num & (~1))

#12. WaP to check if given number is a Palindrome
num = int(input("Enter the number : "))
print("Given no is palindrome") if (str(num) == str(num)[::-1]) else print("Given no is not palindrome")

orig = num
rev1 = 0
while(num):
    rev1 =  (rev1*10) + (num%10)
    num = num//10
print("Reverse of number is {}".format(rev1))
print("Given no is palindrome") if (orig == int(rev1)) else print("Given no is not palindrome")

#13. WaP to print Fibonacci series upto n (n - Accept from user)
def fibonacci(n):
    a,b = 0,1
    while(a < n):
        print(a, end = " ")
        a,b = b,a+b
        
num = int(input("Enter the number : "))
fibonacci(num)

#16. WaP to accept range from user and print all prime numbers in that range
import math
start = int(input("Enter the start of range : "))
end = int(input("Enter the end of range : "))

for i in range(start, end):
    if i < 3 or (not (i & 1)):
        continue
    for j in range(3, int(math.sqrt(i))+1, 2):
        if(i%j == 0):
            break
    else:
        print(i, end=" ")

#17. WaP to accept string from user and count number of consonants in a given string
str1 = input("Enter the string: ")
cnt = 0

for i in str1:
    if i not in ['a','e','i','o','u']:
        cnt += 1
print(cnt)


#List comprehension
#i. List of unique elements
#Ex:     input = [1,3,5,2,1,5,3,7,9,9,7,3]
#    output: [1,2,3,5,7,9]

s = []
[s.append(x) for x in [1,3,5,2,1,5,3,7,9,9,7,3] if x not in s]
print(sorted(s))

#Basic decorators
def decorate(func):
    def wrapper():
        print("Decorator call started")
        func()
        print("Decorator call ended")
    return wrapper

@decorate
def myfunc():
    print("My function called")
    
myfunc()

#Decorator with function argument
def decorate(func):
    def wrapper(*args, **kwargs):
        print("Decorator call started")
        func(args)
        print("Decorator call ended")
    return wrapper

@decorate
def myfunc(num):
    print("My function called with number {}".format(num))
    
myfunc(123, 663 , 446)

#Decorator function with argument & calling function argument
def decorate(msg):
    def wrapper1(func):
        def wrapper(*args, **kwargs):
            print("Decorator call started with message {}".format(msg))
            func(args)
            print("Decorator call ended")
        return wrapper
    return wrapper1

@decorate("Decorator message")
def myfunc(num):
    print("My function called with number {}".format(num))
    
myfunc(123, 663 , 446)
'''
#Decorator function with argument & calling function argument
from functools import wraps
def decorate(msg):    
    def wrapper1(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator call started with message {}, {} ".format(msg, func.__name__))
            func(args)
            print("Decorator call ended")
        return wrapper
    return wrapper1

@decorate("Decorator message")
def myfunc(num):
    print("My function called with number {}".format(num))
    
myfunc(123, 663 , 446)