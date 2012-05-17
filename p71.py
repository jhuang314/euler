#problem 71
import fractions

mult = 999999/7
print 3 * mult - 1

'''
some brute force stuff, too slow

nL = 0
dL = 8

for d in xrange(1000000,999997,-1):
    for n in xrange(3*d/8,d/2+1):
        if nL * d < n * dL and n * 7 < 3 * d:
            nL = n
            dL = d

    print d,nL
gcd = fractions.gcd(nL,dL)
nL /= gcd
dL /= gcd
print "%d/%d" % (nL, dL)
'''
