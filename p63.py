#p63
from math import log10

count = 1
number = 0
for base in xrange(2,11):
    number = base
    exponent = 1
    while int(log10(number))+1==exponent:
        number *= base
        exponent += 1
        count += 1
print count
