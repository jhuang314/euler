# solve problem 64 in python
from math import floor, sqrt
from collections import namedtuple


def getPeriod(s):

    history = set([])

    a0 = floor(sqrt(s))
    if a0 ** 2 == s:
        return 0
    
    # tuple is m, d, a
    t = (0, 1, a0)

    period = 0
 
    while (t not in history):
        history.add(t)
        tprev = t
        period += 1
    
        m = int(tprev[1] * tprev[2] - tprev[0])
        d = int((s - m * m) / tprev[1])
        a = int(floor((a0 + m) / d))
        t = (m, d, a)

    return period-1

print sum([getPeriod(x) % 2 for x in xrange(2, 10000)])



