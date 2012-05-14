#problem 384
from string import *
import cProfile

def aold(oct):
    bin = ''
    for d in oct:
        if d == '0':
            bin += '000'
        elif d == '1':
            bin += '001'
        elif d == '2':
            bin += '010'
        elif d == '3':
            bin += '011'
        elif d == '4':
            bin += '100'
        elif d == '5':
            bin += '101'
        elif d == '6':
            bin += '110'
        elif d == '7':
            bin += '111'
#    bin = lstrip(bin,'0')
    count = 0
    prev = ''
    for d in bin:
        if prev == '1':
            if d == '1':
                count += 1
        prev = d
    return count

cache = {}
for i in range(0,8):
    for j in range(0,8):
        value = 10*i+j
        inp = str(value)
        cache[value]=aold(inp)

def a(x):
    oct = "%o" % x
    bin = ''
    p = '0'
    count = 0
    for d in oct:
        count += cache[int(p+d)]
        p = d
    return count


def b(x):
    if a(x) % 2 == 0:
        return 1
    else:
        return -1
'''
bv = {}

for i in range(0,10000000):
    bv[i]=b(i)
'''

def s(x):
    sum = 0
    for i in range(0,x+1):
        sum += b(i)
    return sum

def g(t,c):
    found = 0
    i = 0
    si = 0
    while (1):
        si += b(i)
        if si == t:
            found += 1
#            print i
            if found == c:
                return i
        i += 1
#print g(54321,1)
#print g(54321,12345)
#print g(1836311903, 1134903170)
#print g(321,50)



fib = 1
prev = 1
sum = 0
for i in range(2,46):
    temp = fib + prev
    prev = fib
    fib = temp
#    gv = g(fib,prev)
#    print "g("+str(fib)+"," + str(prev)+")="+str(gv)
    print fib
#    sum += gv

print sum

