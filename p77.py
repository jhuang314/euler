#problem 77

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]


target = 100
coins = primes(1000)
ways = [1]+[0]*target

for coin in coins:
  for i in range(coin, target+1):
    ways[i] += ways[i-coin]

i=0
for w in ways:
    if w >= 5000:
        print i
        break
    i += 1
