from math import sqrt
'''
def isPrime(x):
    if pow(3,x-1) % x == 1:
        if pow(7,x-1) % x == 1:
            return True
    return False
'''
def isPrime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

pRemain = 10000
currPrime = 1


while pRemain > 0:
    currPrime += 2
    if isPrime(currPrime):
        pRemain -= 1
        

print currPrime


