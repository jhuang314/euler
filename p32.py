#problem 32
import sys

def check(x):
    l = [y for y in range(x,6*x+1,x)]

    a = [list(str(y)) for y in l]
    for y in a:
        y.sort()
    b = [cat(y) for y in a]
    return checkEqual(b)

def cat(lst):
    res = ''
    for y in lst:
        res += y
    return int(res)

def checkEqual(iterator):
      try:
         iterator = iter(iterator)
         first = next(iterator)
         return all(first == rest for rest in iterator)
      except StopIteration:
         return True


sum = 0
s = ['1','2','3','4','5','6','7','8','9']
s.sort(reverse=True)
i=39
j=186
'''
k=i*j
a=list(str(i))
b=list(str(j))
c=list(str(k))
a.extend(b)
a.extend(c)
a.sort()
ped = cat(s)

if cat(a)==ped:
    print i,j,k
sys.exit()
'''

sums = []
for i in range(0,50):
    for j in range(0,10000):
        k=i*j

        a=list(str(i))
        b=list(str(j))
        c=list(str(k))
        a.extend(b)
        a.extend(c)
        a.sort(reverse=True)
        if cat(a)==cat(s):
            print i,j,k
            sum += k
            if k not in sums:
                sums.append(k)

print sum
sum=0
for s in sums:
    sum += s
print sum
