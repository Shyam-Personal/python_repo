def debugmethod(cls):
    print("debug method invoked")
    return cls

@debugmethod
class Base(object):
    pass

class Derived(Base):
    pass

class DebugMethodMeta(type):
    def __init__(self, names, bases, member_dict):
        print("Debug Method Meta Invoked")
        return type.__init__(self, names, bases, member_dict)
    
class BaseMeta(metaclass = DebugMethodMeta):
    pass

class DerivedMeta(BaseMeta):
    pass