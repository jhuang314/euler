#problem 69
from math import sqrt

size = 1000000

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

max = 0
maxn = 0
for n in xrange(2,size):
    frac = 1.0*n/totient(n)
    if frac > max:
        max = frac
        maxn = n

print maxn

