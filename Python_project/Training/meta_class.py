def Add(self):
    return self.no1 + self.no2

def Mul1(self):
    return self.no1 * self.no2

def __init__(self, a, b):
    self.no1 = a
    self.no2 = b
    
def main():
    Arithmetic = type('Arithmetic', (object,), {'__init__':__init__, 'Add':Add, 'Mul':Mul1})
    obj = Arithmetic(10,20)
    print(obj.Add())
    print(obj.Mul())
    
if __name__ == "__main__":
    main()