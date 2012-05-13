#solve problem 57
from math import log10

num = 1L
denom = 2L
temp = 0L
count = 0

for i in range(0,1000):
    num += 2*denom
    temp = num
    num = denom
    denom = temp

    if long(log10(num+denom))-long(log10(denom)) >= 1:
        count += 1

print count
