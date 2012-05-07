#solution for problem 29

from math import *

values = []

for a in range(2,101):
    for b in range(2,101):
        pows = int(pow(a,b))
        if pows not in values:
            values.append(pows)

print len(values)
