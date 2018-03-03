import re

def docstring_grep():
    fh = open("add_num.py")
    data = fh.read()
    #print(data)
    p_obj = re.compile("\"\"\"([\w\s]*)\"\"\"")
    
    for y in p_obj.finditer(data):
        print(y)
        
def without_regex():
    start_of_comment = False
    end_of_comment = False
    docs = ""
    fh = open("add_num.py")
    
    for line in fh:
        y = re.search("\s\"\"\"",line)
        
        if y:
            if start_of_comment == False:
                start_of_comment = True
                #continue
                docs=""
            else:
                start_of_comment = False
                end_of_comment = True
        
        if start_of_comment:
            if (end_of_comment == False):
                print("line is",line)
                docs = docs + line
                print(docs)
            else:
                end_of_comment = False
                docs = ""  
        
            
        '''
        else:
            end_of_comment = False
            
            
        
        if start_of_comment:
            z = re.search("\s\"\"\"",line)
            print(line)
            print("z is " ,z)
            if z:
                end_of_comment = True
                start_of_comment = False
            else:
                docs = docs + line   
        if end_of_comment:
            end_of_comment = False
            start_of_comment = False
            print(docs)
        #else:
                        
            
        
        if y:
            #print(y)
            start_of_comment = True
            continue
        if start_of_comment: 
            cnt =0   
            while(cnt < 10):
                print(line)
                z = re.search("\s\"\"\"",line)
                print("z is " ,z)
                if z:
                    break
                docs = docs + line
                cnt += 1
            #print(docs)
        '''

def main():
    #docstring_grep()
    without_regex()
    
if __name__ == "__main__":
    main()