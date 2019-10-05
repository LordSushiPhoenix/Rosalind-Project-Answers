def fib(n, k):
    if n == 1:
        return 1
    if n == 2:
        return k
    if n <= 4:
        return (fib((n - 1), k) + fib((n - 2), k))
    else:
        return (fib((n - 1), k) + k * fib((n - 2), k))

n = int(input('Enter the month value: '))
k = int(input('Enter the pair value: '))
res = fib(n, k)
print('Result is: %d' % res)