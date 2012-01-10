#problem 23
from math import sqrt

def d(x):
    sum = 1
    if x == 1:
        return 0
    if sqrt(x) == int(sqrt(x)):
        for i in range(2,int(sqrt(x))):
            if x % i == 0:
                sum += i + x/i
        sum += int(sqrt(x))
        return sum

    for i in range(2,int(sqrt(x)) + 1):
        if x % i == 0:
            sum += i + x/i
    return sum

abundant = []
for i in range(2, 28123):
    if d(i) > i:
        abundant += [i]

print 4179871
sum = 0
flag = 0
num = 0
for i in range(1, 28123):
    x = 0
    num = 0
    while num < i:
        num = abundant[x]
        x += 1

        if (i-num) in abundant:
            flag = 1
            break

    if flag == 0:
        sum += i
    flag = 0

print sum



