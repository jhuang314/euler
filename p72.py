#!/bin/python

from math import sqrt

size = 10000001

#modified sieve to store factors
def pfacgen(x):
    sieve = [0]*x
    lim = x/2+1
    i = 2
    for i in xrange(2,lim):
        if sieve[i]==0:
            for j in xrange(i*2,x,i):
                if sieve[j] == 0:
                    sieve[j] = [i]
                else:
                    sieve[j].append(i)
    for k in xrange(2,x):
        if sieve[k]==0:
            sieve[k] = [k]
    return sieve

primes = pfacgen(size)

def totient(x):
    pfacs = primes[x]
    tot = x
    for prime in pfacs:
        tot *= (prime - 1)
        tot /= prime
    return tot


sum = 0
for d in xrange(2,1000001):
    sum += totient(d)

print sum


    
