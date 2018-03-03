'''
14. WaP to accept number from user and check if its a special number or not
Special number is a number in which sum of factorial of the digits is equal to the number.
Ex: 145
1! + 4! + 5! = 145
'''
num = 145
orig = num
special = 0

while(num):
    n = num % 10
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    special = special + fact
    num = num//10

if orig == special:
    print("Special number")
else:
    print("Not Special number")