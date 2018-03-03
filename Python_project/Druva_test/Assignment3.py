fh = open("input1.txt")

for line in fh:
    if len(line.rstrip()) == 28:
        print(line.rstrip())
        break
    
fh.close()