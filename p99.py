#problem 99
from math import log

max = 0
linum = 1
for i in xrange(1,1001):
    pair = [int(x) for x in raw_input().strip().split(',')]
    temp = pair[1] * log(pair[0])
    if temp > max:
        max = temp
        linum = i

print linum
