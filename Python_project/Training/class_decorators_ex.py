def DecorateClass(cls):
    print("Decorator method called")
    cls.added_attribute = "Decorated Attribute"
    cls.empty_list = []
    cls.tuple_1 = (1,2)
    return cls

@DecorateClass
class Test(object):
    
    def __init__(self):
        print("Init of test callled")
        self.id = 1
        
def main():
    
    print(id(Test.added_attribute),id(Test.empty_list))
    print(dir(Test))
    
    obj = Test()
    print(id(obj.added_attribute),id(obj.empty_list),id(obj.id))
    
    obj.added_attribute += "Hello"
    print(id(Test.added_attribute),id(obj.added_attribute))
    
    obj.empty_list.append([1,2,3])
    print(id(Test.empty_list),id(obj.empty_list))
    
    obj.tuple_1 += (3,4)
    print(id(Test.tuple_1),id(obj.tuple_1))
    print(Test.tuple_1,obj.tuple_1)
    
if __name__ == "__main__":
    main()