#problem 12
from math import sqrt
def factor(x):
    num = 0
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            if i == x/i:
                num += 1
            else:
                num += 2
    return num

def triangle(x):
    i = 1
    sum = 0
    while factor(sum) < x:
        sum += i
        i += 1
    print sum
        

triangle(500)
