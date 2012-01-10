#problem 10
from math import sqrt

def isPrime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

sum = 2
for x in range(3,2000000, 2):
    if isPrime(x):
        sum += x

print sum
