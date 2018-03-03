#!/usr/bin/python

#!/usr/bin/python

def DecorateClass(cls):
    cls.added_attribute = "Decorated Attribute"
    return cls

@DecorateClass
class Test(object):
    pass

def main():
    print (Test.added_attribute)    
    print (id(Test.added_attribute))
    print (dir(Test))
    obj = Test()
    print (id(obj.added_attribute))
    obj.added_attribute = "Changed."
    print (dir(obj))
    print(obj.added_attribute)
    print (Test.added_attribute)    
    print (id(obj.added_attribute))
    obj1 = Test()
    print (id(obj1.added_attribute))
    

if __name__ == "__main__":
    main()
