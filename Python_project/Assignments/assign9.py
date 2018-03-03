'''
9. WaP to turnoff right most one bit in a number
'''

def turn_off_rightmost(num):
    print(num ^ 1)

def main():
    num = int(input("Enter the number : "))
    
    turn_off_rightmost(num)

if __name__=="__main__":
    main()