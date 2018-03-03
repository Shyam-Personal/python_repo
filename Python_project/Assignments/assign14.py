'''
14. WaP to accept number from user and check if its a special number or not
Special number is a number in which sum of factorial of the digits is equal to the number.
Ex: 145
1! + 4! + 5! = 145
'''

def fact(num):
    fct = 1
    for i in range(2,num+1):
        fct = fct * i
    return fct

def check_special_num(num):
    orig = num
    sp_num = 0
    while(num):
        sp_num += fact(num%10)
        num = num // 10
        
    if sp_num == orig:
        print("Given no is special number")
    else:
        print("Given no is NOT special number")

def main():
    num = int(input("Enter the number : "))
    check_special_num(num)
    
if __name__ == "__main__":
    main()