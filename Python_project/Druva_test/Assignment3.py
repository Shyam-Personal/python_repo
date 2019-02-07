fh = open("input1.txt")

for line in fh:
    if len(line.rstrip()) == 28:
        print(line.rstrip())
        break
    
fh.close()

with open("input1.txt", "r") as fd:
	for line in fd:
		if len(line.strip()) == 28:
			print(line.strip())
			break