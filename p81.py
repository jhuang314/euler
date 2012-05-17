#problem 81

#classic dynamic programming
input = []
for i in xrange(0,80):
    input.append([int(x) for x in raw_input().strip().split(',')])

dim = len(input)
for i in xrange(1,dim):
    input[0][i] += input[0][i-1]
for i in xrange(1,dim):
    input[i][0] += input[i-1][0]
for i in xrange(1,dim):
    for j in xrange(1,dim):
        input[i][j] += min(input[i-1][j],input[i][j-1])

print input[dim-1][dim-1]
