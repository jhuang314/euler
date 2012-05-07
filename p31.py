#problem 31
#currency=(200,100,50,20,10,5,2,1)
currency=[1,2,5,10,20,50,100,200]

def C(N,M):
    if N==0:
        return 1
    elif N < 0:
        return 0
    elif M <= 0 and N > 0:
        return 1
    else:
        return C(N,M-1)+C(N-currency[M],M)

print C(200,7)
'''
c = [0]+[0]*200
for i in range(1,201):
    j = 0
    ways = 0
    while i-currency[j]>=0 and j < 7:
        ways += c[i-currency[j]]
        j += 1
    c[i]=ways

print c

    
'''
'''
target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [1]+[0]*target
 
for coin in coins:
  for i in range(coin, target+1):
    ways[i] += ways[i-coin]
 
print "Answer to PE31 = ", ways[target]
'''
