'''
36. WaP to accept filename from user and accept number of bytes to be read in alternate fashion
'''

filename = "sample.txt"

fh = open(filename)
text = True
ptr = 0
while(text):
    text = fh.read(14)
    print(text.strip())
    ptr += (15*2)
    fh.seek(ptr)
    