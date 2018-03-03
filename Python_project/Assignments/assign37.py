'''
37. WaP to accept filename from user and print smallest and longest line of the file
'''

filename = "sample.txt"
fh = open(filename)
flag = 1
max_line = ""

for line in fh:
    line = line.strip("\n")
    if flag:
        flag = 0
        small_line = line
        
    if len(max_line) < len(line):
        max_line = line
    if len(small_line) > len(line):
        small_line = line
        
print(small_line)
print(max_line)