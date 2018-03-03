'''
11. WaP to add 2,3,4 or 5 integers
'''

def add(a1, a2, a3 = 0, a4 = 0, a5 = 0):
    return a1 + a2 + a3 + a4 + a5

def main():
    #num = input("Enter space separated numbers : ")
    #a1, a2, a3, a4, a5 = num.split(" ")
    print(add(30,40))
    print(add(50,34,36))
    print(add(12,23,35,60))
    print(add(1,2,3,4,5))    

if __name__=="__main__":
    main()