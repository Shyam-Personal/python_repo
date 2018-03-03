import functools
fh = open("input.txt")

try:
    list2 = list(map(int,fh.readlines()))
    sum1 = functools.reduce(lambda x,y:x+y, list2)
    print(sum1)
except ValueError:
    print("Error")
finally:
    fh.close()
    print("close")