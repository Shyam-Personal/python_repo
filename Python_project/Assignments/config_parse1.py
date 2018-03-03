def input_stats():
    pass

def main():
    
    fh = open("c:\\Users\\cepl-pc\\Desktop\\audio.conf","r")
    
    d1 = {}
    d2 = {}
    
    block =""
    for line in fh: 
        if not line.startswith('#'):
            line = line.rstrip()
            line = line.replace(" ","")
            if line:
                if line.startswith('['):
                    te = line.split('[')
                    block = te[1].rstrip(']')
                    d1[block] = ""
                    d2={}
                else:                    
                    tmp = line.split("=")
                    d2[tmp[0].split("#")[0]] = tmp[1].split("#")[0]
                    d1[block] = d2            
    print(d1)

if __name__ == "__main__":
    main()