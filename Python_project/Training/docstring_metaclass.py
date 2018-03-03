class docstring_validate(type):
    def __init__(self, name, bases, dict1):
        print(dict1)
        
        for key in dict1.keys():
            try:
                if not key.startswith("_"):
                    print(key)
                    if key.__doc__:
                        print("{0} Function has docstring as {1}".format(key, key.__doc__))
                    else:
                        raise NameError ("{0} Function doesn't have docstring".format(key))
            except NameError as e:
                print("{} function doesn't have docstring".format(key))
                

class validate(metaclass = docstring_validate):
    def __init__(self):
        pass
    
    def foo(self):
        """
            This is comment
        """
        pass
    
    def bar(self,abc):
        pass