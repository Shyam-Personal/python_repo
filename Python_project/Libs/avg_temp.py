import re
fh1 = open("input.txt")
lines = fh1.read()
#n=str.rfind("INDIA", start)
#print(n)
fh1.close()

fh = open("input.txt")

dict1 = {}
dict2 = {}
dict3 = {}

for i in fh:
    country1 = i.split(" ")
    
    if country1[0] in dict1.keys():
        dict1[country1[0]] = int(country1[2].rstrip("\n")) + int(dict1[country1[0]])
    else:
        dict1[country1[0]] = country1[2].rstrip("\n")
    
    d = re.findall(country1[0], lines)
    dict2[country1[0]] = int(dict1[country1[0]])/len(d)   
    
    dict3[country1[0]] = len(d) 
print(dict1)
print(dict3)
print(dict2)
fh.close()


fh = open("input.txt")
dict1 = {}

for i in fh:
    country1 = i.split(" ")
    if country1[0] in dict1.keys():
        dict1[country1[0]] = [int(country1[2].rstrip("\n")) + int(dict1[country1[0]][0]), int(dict1[country1[0]][1])+1, (int(country1[2].rstrip("\n")) + int(dict1[country1[0]][0]))/(int(dict1[country1[0]][1])+1)] 
    else:
        dict1[country1[0]] = [country1[2].rstrip("\n"), 1, country1[2].rstrip("\n")]

print(dict1)
fh.close()