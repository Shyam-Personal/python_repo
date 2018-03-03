class test:
    def __init__(self,age,name):
        self.__age = age
        self.name = name
    
    def walk(self):
        pass
    
    
p = test(25,"shyam")

print(p._test__age)
