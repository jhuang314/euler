from itertools import count
from math import sqrt

# initialize
d = 61
x = int(sqrt(d))+1
y = 1
k = x ** 2 - d * (y ** 2)

print x,y,k

m = int(sqrt(d))
while (m ** 2 - d) % k != 0:
    m += 1
print m

x, y, k = float(x * m + d * y)/k, float(x + y * m)/k, float(m ** 2 - d)/k
print x, y, k
x, y, k = x/sqrt(abs(k)), y/sqrt(abs(k)), k/abs(k)
print x, y, k


def compose(t1, t2):
    a, b = t1[0] * t2[0] + d * t1[1] * t2[1], t1[0] * t2[1] + t1[1] * t2[0]
    k1k2 = t1[2] * t2[2]
    return (a/k1k2, b/k1k2, 1)
    


t1 = (x,y,k)
t2 = (x,y,k)
while any(int(z) != z or z < 0 for z in t2):
    t1, t2 = t2, compose(t1,t2)
    print t2



# # compose
# while x != int(x) or y != int(y) or k != 1:
#     x, y = x ** 2 + d * (y ** 2), 2 * x * y
#     x, y = float(x)/abs(k), float(y)/abs(k)
#     k = 1
#     print x, y

# print int(x), int(y)
    
