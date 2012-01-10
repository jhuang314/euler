#problem 20

from math import *

num = factorial(100)
length = int(log(num) / log(10) + 1)

prev = 0L
sum = 0L
for i in range(1, length+1):
    temp = int(num % (pow(10, i)) - prev)
    sum += int((num % (pow(10, i)) - prev) / pow(10,i - 1))
    prev += temp

print sum
print num

mess = "93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000"
s = 0
for c in mess:
    s += int(c)

print s
