'''
5. WaP to accept number from user,accept bit position and also number of bits to turn ON that set of bits in given number
'''

def turn_on_No_of_bits(num,bit_pos,no_of_bits):
    n = 0
    for _ in range(0,no_of_bits):
        y = 1 << bit_pos
        n = n + y
        bit_pos -= 1
    new_num = num | n
    print(new_num)

def main():
    num = int(input("Enter the number : "))
    bit_pos = int(input("Enter the bit : "))
    no_of_bits = int(input("Enter the bit : "))
    
    turn_on_No_of_bits(num,bit_pos,no_of_bits)

if __name__=="__main__":
    main()