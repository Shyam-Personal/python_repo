input1 = 9
input2 = {100, 4, 200, 1, 3, 2, 201, 203, 202, 204}
input2 = sorted(list(input2))
cnt = 1
long_seq = 0
for i in range(len(input2)-1):
  if(long_seq < cnt):
    long_seq = cnt
  if(abs(input2[i+1]-input2[i]) == 1):
    cnt += 1
    continue
  cnt = 2
print(long_seq)
'''
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.info('Hello baby')

list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(len(list1)):
  for j in range(len(list1[0])):
    print(list1[i][j], end = " ")
  print()
print()

j = len(list1[0])-1
for i in range(len(list1)):
  list1[i][i], list1[i][j] = list1[i][j], list1[i][i]
  j -= 1
#for i, j in zip(range(len(list1)), range(len(list1[0])-1, -1, -1)):
#    list1[i][i], list1[i][j] = list1[i][j], list1[i][i]

for i in range(len(list1)):
  for j in range(len(list1[0])):
    print(list1[i][j], end = " ")
  print()
print()

list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]	
for i in range(len(list1)):
  for j in range(i+1, len(list1[0])):
    list1[i][j], list1[j][i] = list1[j][i], list1[i][j]

for i in range(len(list1)):
  for j in range(len(list1[0])):
    print(list1[i][j], end = " ")
  print()
print()


import test
from test import test_method

test_method()

import sys

def abc():
  try:
    print("try")
    #sys.exit()
    return
  except:
    print("exception")
  else:
    print("else")
  finally:
    print("final")

class A:
  def __init__(self):
    pass

  def foo(self):
    print("A foo")

class B(A):
  def __init__(self):
    pass

  def foo(self):
    print("B foo")

class C(B):
  def __init__(self):
    pass

  def foo(self):
    print("C foo")
	
if __name__ == "__main__":
  #abc()
  ob = C()
  ob.foo()
  super(C,ob).foo()
  super(B,ob).foo()
'''