class ManagerMeta(type):
    def __init__(self, name, bases, dict1):
        manager_init_method = False
        manager_del_method = False
        
        print(dict1)
        
        for key in dict1.keys():
            if key == "__init__":
                manager_init_method = True
            elif key == "__del__":
                manager_del_method = True
                
        if not manager_init_method or not manager_del_method:
            raise NameError ("Constructor or Destructor not found")
        else:
            print("Constructor & destructor found for {} class".format(name))
        return type.__init__(self, name, bases, dict1)

class Test (metaclass = ManagerMeta):
    def __init__(self):
        pass
    
    def __del__(self):
        pass
    
class Test2 (metaclass = ManagerMeta):
    pass
