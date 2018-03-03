import sys
L1=[]

def isFull():
    if(len(L1) >= 10):
        return True
    else:
        return False

def isEmpty():
    if(not L1):
        return True
    else:
        return False

def push(data):
    if (not isFull()):
        L1.append(data)
        print(L1)
    else:
        print("Stack is Full!!")

def pop():
    if (not isEmpty()):
        L1.pop()
        print(L1)
    else:
        print("Stack is Empty!!")

def display():
    print(L1)
    
def peep():
    if (not isEmpty()):
        print(L1)
        return L1[-1]        
    else:
        print("Stack is Empty!!")    
    
def main():
    while(1):
        print(" ****** Menu ******** \n1) Push Data \n2) Pop Data \n3) Display \n4) Peep \n5) Exit")
        c = int(input("Please Enter the choice: "))
        
        if (c == 1):
            data = int(input("Please Enter the data to be pushed: "))
            push(data)
        elif (c == 2):
            pop()
        elif (c == 3):
            display()
        elif (c == 4):
            print(peep())
        elif (c == 5):
            print("Successfully Exited!! ")
            sys.exit()
        else:
            print("Please enter correct choice !!")
        
if __name__ == "__main__":
    main()