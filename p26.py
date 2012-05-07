#solution for problem 26
from eulerF import *
import fractions

def recurringCycle(x):
    for i in range(1,x+1):
        if fractions.gcd(10,i) == 1 and isPrime(i):
            3
#the key is cyclic numbers, and 983 is largest generating cyclic number under 1000
'''
Algo for computing

Let b be the number base (10 for decimal)
Let p be a prime that does not divide b.
Let t = 0.
Let r = 1.
Let n = 0.
loop:

    Let t = t + 1
    Let x = r · b
    Let d = int(x / p)
    Let r = x mod p
    Let n = n · b + d
    If r ≠ 1 then repeat the loop.

if t = p − 1 then n is a cyclic number.


'''
