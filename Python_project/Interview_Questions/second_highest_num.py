import random
numbers = random.sample(range(1000),20)
#numbers = [6,5,9,2,8,9,10,6,5,10,10,2,3,10,8,3,4]

print(sorted(numbers))
print(numbers)

if numbers[0] > numbers[1]:
    last, second = numbers[0], numbers[1]
else:
    last, second = numbers[1], numbers[0]
        
for n in numbers[2:]:
    if n > last:
        last, second = n, last
    elif last > n > second:
        second = n
print(second, last)