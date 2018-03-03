#12. WaP to check if given number is a Palindrome

def main():
    a = int(input("Enter no : "))
    b=[]
    
    while(a):
        d = a % 10
        b.append(d)
        a = a // 10
    j=-1   
    for x in range(0,len(b)//2):
        if not b[x] == b[j]:
            return ("No is not Palindrome")
        j -= 1
    return ("No is palindrome")

if __name__=="__main__":
    print(main())