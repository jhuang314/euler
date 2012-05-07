#solution for problem 30

from math import pow

sum = 0

for x5 in range(0, 10):
    for x4 in range(0, 10):
        for x3 in range(0, 10):
            for x2 in range(0, 10):
                for x1 in range(0, 10):
                    for x0 in range(0, 10):
                        if (pow(x5,5) + pow(x4,5) + pow(x3,5) + pow(x2,5) + pow(x1,5) + pow(x0,5)) == (x5 * 100000 + x4 * 10000 + x3 * 1000 + x2 * 100 + x1 * 10 + x0) :
                            value =  x5 * 100000 + x4 * 10000 + x3 * 1000 + x2 * 100 + x1 * 10 + x0
                            print value
                            sum += value

print sum - 1
print x5 * 100000 + x4 * 10000 + x3 * 1000 + x2 * 100 + x1 * 10 + x0
