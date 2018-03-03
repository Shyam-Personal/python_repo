def main():
    num = int(input("Enter the number: "))
    revn = 0
        
    while num:
        y = num%10
        revn = revn*10 + y
        num = num // 10
    print(revn)        
              
if __name__ == "__main__":
    main()