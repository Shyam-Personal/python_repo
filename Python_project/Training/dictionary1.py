def dict_key(dict2,data):
    dict3={}
    if (isinstance(dict2,dict)):
        if(isinstance(data, tuple) or isinstance(data, list)):
            j = 0
            length = len(data)
            for i in dict2.keys():
                data1 = None
                if (j < length):
                    data1 = data[j]
                    j +=1
                dict3[i] = data1 
            return dict3            
              
        else:
            return dict2.fromkeys(dict2,data)
    else:
        print("first argument should be dictionary")
            

def main():
    dict1 = {"name":"Shyam","city":"pune","phone":"9789758765"}
    
    print(dict_key(dict1,('shhhh','test')))

if __name__ =="__main__":
    main()