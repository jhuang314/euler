#problem 25

def fib():
    n = 12
    p = 1L
    c = 1L

    for i in range(3,n + 1):
        t = p + c
        p = c
        c = t
    return c


