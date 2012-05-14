#problem 50
from math import sqrt

def isPrime(x):
    if x == 2:
        return True
    if x < 3 or x % 2 == 0:
        return False
    lim = int(sqrt(x)+1)
    for i in range(3,lim,2):
        if x % i == 0:
            return False
    return True

primes = []
limit = 1000000

for i in range(0,limit):
    if isPrime(i):
        primes.append(i)

max = 0
streak = 1
maxprime = 0
lim = len(primes)
for size in range(2,lim):
    sum = 0
    index = 0
    for i in range(0,size):
        sum += primes[i]
    
    if sum < limit:
        while index < lim-1 and primes[index]<sum:
            index += 1
        if primes[index] == sum:
            maxprime = sum
            max = size
        else:
            index -= 1
    else:
        break
    for i in range(0,lim-size):
        sum += primes[i+size]
        sum -= primes[i]
        if sum >= limit:
            break
        while index < lim-1 and primes[index]<sum:
            index += 1
        if primes[index] == sum:
            maxprime = sum
            max = size
            break
        else:
            index -= 1
    
print maxprime
