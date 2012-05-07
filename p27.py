#solution for problem 27
from eulerF import *

def numPrimes(func):
    i = 0
    fvalue = func(i)
    while fvalue > 1 and isPrime(func(i)):
        i = i + 1
        fvalue = func(i)
    return i


ranges = 10
max = dict({'a':0, 'b':0, 'primes':0})
for a in range(-999,1000):
    for b in range(-999,1000):
        poly = lambda n: n*n + a*n + b
        primes = numPrimes(poly)
        if max['primes'] < primes:
            max['a'] = a
            max['b'] = b
            max['primes'] = primes

print max


