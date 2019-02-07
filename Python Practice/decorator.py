'''
#1
import operator

def person_lister(f):
    def inner(people):
        #complete the function
        list = [];
        people = sorted(people,key=lambda l:l[2])
        for i in people:
            list.append(f(i))
        return list
    return inner
	
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#2
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
	
op = my_gen()
for i in op:
  print(i)
 

def trace(func):
	def inner(*args, **kwargs):
		print ('>>')
		func(*args, **kwargs)
		print ('<<')
	return inner

@trace
def func1(x, y):
	print ('x:', x, 'y:', y)
	func2((x, y))

@trace
def func2(content):
	print ('content:', content)

def test():
	func1('aa', 'bb')

test()


import time


def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


print(my_function())
'''
from time import sleep


def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

for num in range(1, 6):
    print(print_number(num))
'''

list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(len(list1)):
	for j in range(len(list1[0])):
		print(list1[i][j], end=" ")
	print()
	
list2 = []
for i in range(len(list1)):
	list3 = []
	for j in range(len(list1[0])):
		list3.append(list1[j][i])
	list2.append(list3)

print("\n")
for i in range(len(list1)):
	for j in range(len(list1[0])):
		print(list2[i][j], end=" ")
	print()
'''