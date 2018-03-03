def seek_fun(ptr,step):
    fh = open("c:\\Users\\cepl-pc\\Desktop\\test_byte.txt","r")
    
    for line in fh:    
        fh.seek(ptr,0)
        line=fh.readline(step)
        print(line)
        ptr += 2*step
    fh.close()
    
def main():
    print("First ")
    seek_fun(0,10)
    print("skip first")
    seek_fun(10,10)
        
       
if __name__ == "__main__":
    main()
    
'''
34. WaP to accept a filename from user, open that file in read mode and print lines in reverse order
''

def main():
    fh = open("test.py",'r')
    ptr = 12
    x = fh.read(ptr)
    while x:
        ptr = ptr + 13
        print(x.strip())
        fh.seek(ptr)
        x = fh.read(13)
    fh.close()
    

if __name__ == "__main__":
    main()
'''