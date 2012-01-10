sum = 0

fib = 1
prev = 1

while fib < 4000000:
	temp = fib + prev
	prev = fib
	fib = temp
	if fib % 2 == 0:
		sum += fib
print sum
