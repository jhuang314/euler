#problem 25
from eulerF import *


def fibonacciG(n):
    root5 = sqrt(5)
    phi = 0.5 + root5/2
    return long(0.5 + phi**n/root5)

def fib(n):

    p = 1L
    c = 1L

    for i in range(3,n + 1):
        t = p + c
        p = c
        c = t
    return c

def f(n):
    i = 3
    while 1:
        if length(fibonacci(i)) == n:
            return i
        i = i + 1

print f(1000)
#print fibonacci(1000)


