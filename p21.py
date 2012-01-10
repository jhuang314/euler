#problem 21
from math import sqrt

def d(x):
    sum = 1
    if x == 1:
        return 0
    if sqrt(x) == int(sqrt(x)):
        for i in range(2,int(sqrt(x))):
            if x % i == 0:
                sum += i + x/i
        sum += int(sqrt(x))
        return sum

    for i in range(2,int(sqrt(x)) + 1):
        if x % i == 0:
            sum += i + x/i
    return sum

sum = 0
for i in range(3,10000):
    other = d(i)
    if d(other) == i and i != other:
        print i
        sum += i

print sum
