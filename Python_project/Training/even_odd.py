def main():
    n = int(input("Enter the no: "))
    
    if n % 2:
        print("Given no is Odd")
    else:
        print("Given no is Even")
        
    digit = n %10
    if digit not in [0,2,4,6,8]:
        print("Given no is Odd")
    else:
        print("Given no is Even")
        
        

if __name__ == "__main__":
    main()