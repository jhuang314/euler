from itertools import count
from math import sqrt

def minSol(d):
    for y in count(2,1):
        x = sqrt(1 + d * (y**2))
        if x == int(x):
            return x

maxX = 0
index = 0
for i in xrange(2,1001):
    if int(sqrt(i)) ** 2 == i:
        continue
    res = minSol(i)
    if res > maxX:
        maxX = res
        index = i
    print i

print maxX, index
