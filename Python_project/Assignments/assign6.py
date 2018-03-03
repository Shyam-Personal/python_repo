'''
6. WaP to accept number from user and accept bit position to TOGGLE in given number
'''

def toggle_bit(num, bit):
    x = 1 << bit
    print(num ^ x)

def main():
    num = int(input("Enter the number : "))
    bit = int(input("Enter the bit : "))
    
    toggle_bit(num, bit)

if __name__=="__main__":
    main()