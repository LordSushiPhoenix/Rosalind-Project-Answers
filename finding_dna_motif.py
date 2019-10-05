s = "GATATATGCATATACTT"
t = "ATAT"
n = 0
nlist = []
'''
for i in range(0, int(len(s) / len(t))):
    n = s.find(t[n:])
    if n == -1 or n in nlist:
        break
    nlist.append(n)
    print(n)
'''
for i in range(0, len(s) - len(t)):
    for j in range(0, len(t) + 1):
        if s[i+j] != t[j]:
            break

    print(i)
