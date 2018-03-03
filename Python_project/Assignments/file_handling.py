def input_stats():
    pass

def main():
    
    fh = open("c:\\Users\\cepl-pc\\Desktop\\hits.txt","r")
    
    maxline = ""
    for line in fh: 
        length = len(line)
        if len(maxline) < length:
            maxline = line
            
    print(maxline)


if __name__ == "__main__":
    main()