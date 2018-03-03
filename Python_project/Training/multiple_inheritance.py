import inspect
class Base:
    def Print(self):
        print("Print of base")
        
class A(Base):
    def Display(self):
        print("Display of A")
        
    def Foo(self):
        print("In foo")
        
class B(object):
    def Print(self):
        print("Print of B")
    
    def Display(self):
        print("Display of B")
        
class C(A,B):
    pass

class D(B,A):
    pass

x = C()

x.Display()
x.Print()

print(inspect.getmro(C)) #method to find method resolution order