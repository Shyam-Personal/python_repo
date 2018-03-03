def main1():
    fp  = open("occur.txt")
    d1 ={}
    for line in fp:
        line = line.rstrip("\n")
        for char in line:
            if char in d1.keys():
                d1[char] += 1
            else:
                d1[char] = 1
        
    print(d1)

def main():
    fp  = open("occur.txt")
    d2 = {'max_occur' : 1, 'char' : ""}
    cont_occur = 1
    for line in fp:
        line = line.rstrip("\n")
        line = line.replace(" ","")
        for i in range (1,len(line)):
            if line[i] == line [i-1]:
                cont_occur += 1
                if d2['max_occur'] < cont_occur :
                    d2['max_occur'] = cont_occur 
                    d2['char'] = line[i-1]              
            else:
                if line[i-1] == line [i-2]:       
                    d2['max_occur'] += 1
                cont_occur = 1                       
    print(d2)

if __name__ == "__main__":
    main()