#problem 60
import eulerF
from math import sqrt

def esieve(x):
    primes = []
    sieve = [0]*x
    lim = int(sqrt(x))+1
    i = 2
    for i in xrange(2,lim):
        if sieve[i]==0:
            primes.append(i)
            for j in xrange(i*i,x,i):
                sieve[j] = 1
    for k in xrange(i,x):
        if sieve[k]==0:
            primes.append(k)
    return primes

primes = esieve(700000)
