import re

fh = open("input.txt")
readfile = fh.read()
fh.close()

file = open("input.txt")
dict1 = {}
for line in file:
    #print(line)
    line = line.strip("\n")
    word = line.split(" ")
    #print(word)
    
    for i in range(0,len(word)):
        if word[i] not in dict1.keys():
            #pass
        #else:
            cnt = re.findall(word[i],readfile)
            dict1[word[i]] = len(cnt)
            #print(word[i])
            
print(dict1)
file.close()

fh = open("input.txt")
dict2 = {}
for line1 in fh:
    words = line1.split()
    for i in range(len(words)):
        if(words[i] not in dict2.keys()):
            dict2[words[i]] = 1
        else:
            dict2[words[i]] += 1
print(dict2)
fh.close()