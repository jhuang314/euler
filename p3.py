from math import sqrt


def isPrime(x):
	if pow(3,x-1) % x == 1:
		if pow(7,x-1) % x == 1:
			return True
	return False


num = 600851475143
up = sqrt(num)
factors = []
for x in range(1,int(up)):
	if num % x == 0:
		factors += [x]

notprime = []
for x in factors:
	if isPrime(x):
		print x

