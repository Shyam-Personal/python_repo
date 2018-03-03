#!/usr/bin/python

class Test(object):
    def Foo():
        print("Static Method")
    f = staticmethod(Foo)
c = Test()
#Test.Foo()
#c.Foo()
c.f()

class TestStaticDecorator(object):
    @staticmethod
    def Foo():
        print("Static Method")

c = TestStaticDecorator()
c.Foo()

class TestStatic():
    def Foo():
        print("Static Method")
    f = staticmethod(Foo)
c = TestStatic()
#TestStatic.Foo()
#c.Foo()
c.f()

