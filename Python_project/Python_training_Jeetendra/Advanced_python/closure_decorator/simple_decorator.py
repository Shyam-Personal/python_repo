#!/usr/bin/python

def InitGenerator(func):
    def initialize(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return initialize

def ToUpper():
    while True:
        string = yield # coroutines
        print(string.upper())

@InitGenerator
def ToUpperDecorated():
    while True:
        string = yield
        print(string.upper())

z = ToUpper()
next(z)
z.send("Hello")

y = InitGenerator(ToUpper)
x = y()
x.send("Hello")

x = ToUpperDecorated()
x.send("hello")
x.close()
#x.send("hello") #StopIteration
#print (x.send("hello"))
