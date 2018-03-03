#WaP to accept number from user and accept bit position to turn OFF in given number

def turn_off(num,bit):
    x = ~(1 << bit)            
    new_num = num & x
    print(new_num)

def main():
    num = int(input("Enter the number : "))
    bit = int(input("Enter the bit : "))
    
    turn_off(num,bit)

if __name__=="__main__":
    main()