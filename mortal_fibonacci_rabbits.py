def mortFib(n, k):
    if n <= 2:
        return 1
    if n <= k:
        return (mortFib((n - 1), k) + mortFib((n - 2), k))
    elif n == (k+1):
        return (mortFib((n - 1), k) + mortFib((n - 2), k) - 1)
    else:
        return (mortFib((n - 1), k) + mortFib((n - 2), k) - mortFib((n-(k+1)), k))

n = int(input('Enter the month value: '))
k = int(input('Enter the life value: '))
res = mortFib(n, k)
print('Result is: %d' % res)