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