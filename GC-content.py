import operator
datafile = open("GC-data.txt", "r")
theStrings = {}
countedStrings = {}
for line in datafile:
    if line.startswith('>'):
        genes = next(datafile)
        theStrings[line] = genes
##print(theStrings)
for aKey, aVal in theStrings.items():
    n = 0.0
    gc = 0.0
    nTides = list(aVal)
    for nTide in nTides:
        n += 1.0
        if nTide in "gcGC":
            gc += 1.0
    countedStrings[aKey] = (gc/n)

v = list(countedStrings.values())
k = list(countedStrings.keys())
print(k[v.index(max(v))])
print(max(v) * 100)
