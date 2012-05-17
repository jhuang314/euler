#problem 58
from eulerF import isPrime

gap = 4  #keeps track of gap between edges of spiral
col = 3  #keeps track of size of spiral (from middle to one end)
value = 13 #keeps track of the upper right most diagonal value
numPrimes = 3
diagsize = 5
while 10*numPrimes >= diagsize:
    for i in xrange(0,3):
        if isPrime(value + i*gap):
            numPrimes += 1
    diagsize += 4

    #compute next 4 diag values
    value = value + gap * 4 + 2
    gap = gap + 2
    col += 2
    
print col



