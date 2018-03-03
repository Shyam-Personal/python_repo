'''
34. WaP to accept a filename from user, open that file in read mode and print lines in reverse order
'''

def file_straight():
    fh = open("test.py",'r')
    ptr = 0
    x = 1
    while x:
        x = fh.readline()
        ptr = ptr + len(x)
        print(x.replace("\n", ""))
        fh.seek(ptr)
    fh.close()

def file_reverse():
    fh = open("test.py",'r')
    fh.seek(0,2)
    line = ""
    ptr = fh.tell()
    
    while(ptr):
        next_char = fh.read(1)
        if next_char == "\n":
            print(line[::-1])
            line = ""
        else:
            line = line + next_char
        ptr -= 1
        fh.seek(ptr)
    line = line + next_char
    print(line[::-1])
    fh.close()
    
def main():
    
    if input("Enter 1 for straight or 2 for reverse : ") == "1":
        file_straight()
    else:
        file_reverse()
    
if __name__ == "__main__":
    main()