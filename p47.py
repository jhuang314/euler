#problem 47

from math import sqrt
import cProfile

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
size = 2000000



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
                
def solve(x):
    sieve = [0]*x
    lim = int(sqrt(x))+1
    for i in xrange(2,lim):
        if sieve[i]==0:
            for j in xrange(i*2,x,i):
                sieve[j] += 1
    for k in xrange(2,x):
        if sieve[k:k+4]==[4,4,4,4]:
            print k
            return k
    return k

solve(size)


def pfactor(x):
    pfactors = []
    num = 0
    for p in primes:
        if p > x:
            return pfactors
        if x % p == 0:
            pfactors.append(p)
            num += 1
            return pfactors
    return pfactors

'''    
This works, but is just too slow...
temp = []
streak = 0
limit = 4
for i in range(2,size):
    pf = pfactor(i)
    if i % 10000 == 0:
        print i
    if len(pf) == limit:
        streak += 1
        temp.append(pf)
    else:
	streak = 0
        temp = []
    if streak == limit:
	print i-3,temp
        exit()
'''
