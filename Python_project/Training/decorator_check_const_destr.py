def VerifyManagerMethods(cls):
    def wrapper():
        manager_init_method = False
        manager_del_method = False
        
        print(cls.__dict__)
        
        for key in cls.__dict__.keys():
            if key == "__init__":
                manager_init_method = True
            elif key == "__del__":
                manager_del_method = True
                
        if not manager_init_method or not manager_del_method:
            raise NameError ("Constructor or Destructor not found")
        else:
            print("Constructor & Destructor found")
        return cls
    return wrapper

@VerifyManagerMethods
class Test:
    def __init__(self):
        pass
    
    def __del__(self):
        pass
    
@VerifyManagerMethods
class Test2:
    pass

t = Test()
t2 = Test2()