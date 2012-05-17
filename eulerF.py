#useful functions for project euler
from math import *
import sys
import random

def length(x):
    logs = ceil(log10(x))
    return int(logs)


# Returns F(n)
def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


# Returns a tuple (F(n), F(n+1))
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n / 2)
        c = a * (2 * b - a)
        d = b * b + a * a
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

'''
def isPrime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
'''



def toBinary(n):
    r = []
    while (n > 0):
        r.append(n % 2)
        n = n / 2
    return r

def test(a, n):
    """
    test(a, n) -> bool Tests whether n is complex.
    
    Returns:
    - True, if n is complex.
    - False, if n is probably prime.
    """
    b = toBinary(n - 1)
    d = 1
    for i in xrange(len(b) - 1, -1, -1):
        x = d
        d = (d * d) % n
        if d == 1 and x != 1 and x != n - 1:
            return True # Complex
        if b[i] == 1:
            d = (d * a) % n
    if d != 1:
        return True # Complex
    return False # Prime

def isPrime(n):
    """
    MillerRabin(n, s = 1000) -> bool Checks whether n is prime or not
    
    Returns:
      - True, if n is probably prime.
      - False, if n is complex.
      """
    s = 50
    for j in xrange(1, s + 1):
        a = random.randint(1, n - 1)
        if (test(a, n)):
            return False # n is complex
    return True # n is prime

def pfactorexp(x):
    pfactors = []
    for p in primes:
        if p > x:
            return pfactors
        if x % p == 0:
            exp = 1
            x /= p
            while x % p == 0:
                x /= p
                exp += 1
            pfactors.append((p,exp))
    return pfactors

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
