'''
15. WaP to print following patterns:
'''

def a():
    '''
    1
    1    2
    1    2    3
    1    2    3    4
    '''
    print("$$$$$$     A    $$$$$$" )
    for i in range (1,5):        
        for j in range(1,i+1):
            print(j,end="    ")
        print()
        
def b():
    '''
    a
    a    b
    a    b    c
    '''
    print("$$$$$$     B    $$$$$$" )
    for i in range(1,4):
        for j in range(1,i+1):
            print(chr(96+j),end="    ")
        print()
        
def d():
    '''
    d. *     *      *      *
          *      *      *
             *      *
                 *
    '''
    print("$$$$$$     D    $$$$$$" )
    for i in range(0,4):
        tabs = "\t"*i
        for j in range(4,i,-1):
            print(tabs + '*',end="")
            tabs = "\t"*2
        print()
        
def e():
    '''
    
    e.  *
        *      *
        *      *       *
        *      *       *       *
    '''
    print("$$$$$$     E    $$$$$$" )
    for i in range(1,5):
        for _ in range(i):
            print("*" + "\t", end="")
        print()
       
def f():
    '''
    f.                      *
                      *            *
               *            *            *
        *            *            *             *
    '''
    print("$$$$$$     F    $$$$$$" )
    for i in range(4,0,-1):
        tabs = "\t"*(i-1)
        for j in range(4,i-1,-1):
            print(tabs + "*", end="")
            tabs = "\t"*2
        print()
    
def main():
    a()
    b()
    d()
    e()
    f()
    
if __name__ == "__main__":
    main()