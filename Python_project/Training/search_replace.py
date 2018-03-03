def main():
    a = input("Enter string: ")
    s = input("Enter search char: ")
    r = input("Enter replace char: ")
    b=""
    
    for i in a:
        if i == s:
            b += r
        else:
            b += i
                              
    
    print(b)

if __name__ == "__main__":
    main()