#problem 92
import cProfile

def chain(num):
    while num != 1 and num != 89:
        sum = 0
        while num > 0:
            sum += (num % 10)**2
            num /= 10
        num = sum
    return num

count = 0
for i in xrange(1,10000000):
    if chain(i) == 89:
        count += 1

print count
