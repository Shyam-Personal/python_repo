import pickle

def main():
    d1 = {'a':1,'b':2,'c':3}
    d2 = {'name':"shyam","age":30}
    
    bytes_data = pickle.dumps(d1)
    pickle.loads(bytes_data)
    
    fd = open("stext.txt",'ab')    
    pickle.dump(d1,fd)
    pickle.dump(d2,fd)
    fd.close()
    
    fd = open("stext.txt",'rb')
    
    try:
        while True:
            print(pickle.load(fd))
    except EOFError:
        fd.close()
        
if __name__ == "__main__":
    main()