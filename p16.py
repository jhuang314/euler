#problem 16
from math import log

num = pow(2,15)
length = int(log(num) / log(10) + 1)

prev = 0
sum = 0
for i in range(1, length+1):
    temp = num % (pow(10, i)) - prev
    sum += (num % (pow(10, i)) - prev) / pow(10,i - 1)
    prev += temp

print sum
