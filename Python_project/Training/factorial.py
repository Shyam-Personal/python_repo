def main():
    
    n = 1
    while (n != -1):
        n = int(input("Enter no: (Enter  for exit): "))
        fact = 1
        while (n > 0):
            fact = fact * n        
            n = n - 1
        
        print(fact)

if __name__ == "__main__":
    main()