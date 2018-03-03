def toUpper():
    while True:
        string = yield
        print(string.upper())

def main():
    z = toUpper()
    next(z)
    z.send(" hello shyam")
    z.send(" hello shyam next")
    
if __name__ == "__main__":
    main()