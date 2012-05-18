#problem 62
from math import log10

size = 10000
target = 5
cubes = []
for b in xrange(1,size):
    cubes.append(b**3)

def isPerm(a,b):
    astr = "".join(sorted(str(a),reverse=True))
    bstr = "".join(sorted(str(b),reverse=True))
    lim = len(astr)
    if len(bstr) != lim:
        return False
    for i in xrange(0,lim):
        if astr[i] != bstr[i]:
            return False
    return True

count = 1
for i in xrange(0,size):
    for j in xrange(i+1,size-1):
        if int(log10(cubes[i])) < int(log10(cubes[j])):
            break
        if isPerm(cubes[i],cubes[j]):
            count += 1
    if count == target:
        print cubes[i]
        exit()
    else:
        count = 1

