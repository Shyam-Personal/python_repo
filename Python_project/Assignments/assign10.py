'''
10. WaP to count number of 1 bits in a given number
'''

def no_of_ones(num):
    cnt = 0
    for i in range(15):
        bit = 1 << i
        n = num & bit
        if n != 0:
            cnt += 1
            
    print(cnt)

def main():
    num = int(input("Enter the number : "))
    if (num > 65535):
        print("Out of range (0-65535) ")
    else:
        no_of_ones(num)

if __name__=="__main__":
    main()