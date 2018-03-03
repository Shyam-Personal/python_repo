class FileIterator:
    def __init__(self, file_name, decrypt_key):
        self.fd = open(file_name)
        self.decrypt_key = decrypt_key
        
    def __decrypt(self,line):
        return self.line
    
    def __next__(self):
        line = self.fd.readline()
        self.decrypt_key(line)
        if line == "":
            raise StopIteration
        return line
    
    def next(self):
        """ Python 2.7 needs next to make class iterable """
        return self.__next__()
    
def main():
    file_name = input("Enter he file name : ")
    obj = FileIterator(file_name,5)
    obj_iterator = iter(obj)
    
    print(next(obj_iterator)) #3.x : __next__ method
    print(next(obj_iterator))
    
if __name__ == "__main__":
    main()