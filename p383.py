#solve problem 383

def f5(n):
    x = 1L
    base = 5L
    max = 0L
    while base <= n:
        if n % base == 0:
            max = x
        base *= 5
        x += 1
    return max

def f5p(n):
    count = 0L
    while n%5==0:
        n /= 5
        count += 1
    return count

'''
for i in range(5,1000,5):
    tally=''
    for j in range(0,f5p(i)):
        tally+='0'
    print str(i)+":\t"+tally
'''

def f5facold(n):
    count = 0
    for i in range(5L,n+1L,5):
        count += f5p(i)
    return count

def f5fac(n):
    count = n/5L
    base = 25
    while n-base >= 0:
        count += long(n/base)
        base *= 5
    return count

def fac(n):
    res = 1L
    for i in range(1L,n+1L):
        res *= i
    return res


#print f5p(fac(200000))

def t5(n):
    count = 0L
    prev = 0L
    for i in range(5,n+1,5):
        if f5fac(2*i-1) < 2*f5fac(i):
            count += 1
#            print str(i)+":\t"+str(i-prev)+"=\t"+str(f5fac(2*i-1))+"<"+str(2*f5fac(i))
            prev = i
    return count

x = 5
for i in range(5,1001,5):
    print str(i)+":\t"+str(t5(i))



'''
print t5(x)

def t5p(n):
    n *= 2
    count = n/5L
    count -= n/25L+1
    count /= 2
    print count

t5p(x)
'''
