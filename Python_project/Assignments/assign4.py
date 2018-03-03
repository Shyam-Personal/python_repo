'''
4. WaP to accept number from user and accept bit position to turn ON in given number
'''

def turn_on(num,bit):
    x = (1 << bit)            
    new_num = num | x
    print(new_num)

def main():
    num = int(input("Enter the number : "))
    bit = int(input("Enter the bit : "))
    
    turn_on(num,bit)

if __name__=="__main__":
    main()