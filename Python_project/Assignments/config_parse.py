def input_stats():
    pass

def main():
    
    fh = open("c:\\Users\\cepl-pc\\Desktop\\audio.conf","r")
    
    d1 = {}
    for line in fh: 
        if not line.startswith('#') and not line.startswith('['):
            line = line.rstrip()
            line = line.replace(" ","")
            if line:
                tmp = line.split("=")
                d1[tmp[0].split("#")[0]] = tmp[1].split("#")[0]
            
    print(d1)


if __name__ == "__main__":
    main()