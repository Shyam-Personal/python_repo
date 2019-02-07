n = 13
fib = []
for i in range(n):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else:
        fib.append(fib[i-1] + fib[i-2])
print(fib)

def fibo(x):
	a, b = 0, 1
	for i in range(x):
		yield a
		a, b = b, a + b
		
print(list(fibo(12)))