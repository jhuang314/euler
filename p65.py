#problem 65

groups = 33 #or 3


num = 0L
denom = 1L
for k in xrange(groups,0,-1):
    num += denom #add 1

    #swap
    temp = denom
    denom = num
    num = temp

    num += denom * 2 * k #add 2k

    #swap
    temp = denom
    denom = num
    num = temp

    num += denom #add 1

    #swap
    temp = denom
    denom = num
    num = temp



num += 2 * denom #add 2

sum = 0
while num > 0:
    sum += num % 10
    num /= 10
print sum
