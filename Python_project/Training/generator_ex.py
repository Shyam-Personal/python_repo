def Increment(n):
    for x in n:
        yield x
        
def main():
    c = Increment(range(10))
    print(c)
    
    print(type(c))
    print(next(c))
    
if __name__ == "__main__":
    main()