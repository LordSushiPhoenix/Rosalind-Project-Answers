'''
#exponential complexity recursion yay
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
'''
#S P E E D B O I
def mortFib(n, k, ar):
    i = 0
    while i < n:
        #print(i)
        if i <= 1:
            ar.append(1)
        elif i < k:
            ar.append(ar[i - 1] + ar[i - 2])
        elif i == (k):
            ar.append(ar[i - 1] + ar[i - 2] - 1)
        else:
            ar.append(ar[i - 1] + ar[i - 2] - ar[i - (k + 1)])
        i += 1
    #print('list built')
    #for j in ar:
    #    print(j)
    return ar[n-1]

n = int(input('Enter the month value: '))
k = int(input('Enter the life value: '))
pop = []
res = mortFib(n, k, pop)
print('Result is: %d' % res)