#problem 82

input = []
for i in xrange(0,80):
    input.append([int(x) for x in raw_input().strip().split(',')])

dim = len(input)

col = [0 for i in xrange(0,dim)]
for column in xrange(1,dim):
    for row in xrange(0,dim):
        #compute distances from each element in prev column
        dist = [input[row][column-1]]
        sums = 0#sum of column distance of elements in same column
        for r in xrange(row+1,dim):
            sums += input[r][column]
            dist.append(input[r][column-1]+sums)#add row distance to sums

        sums = 0
        for r in xrange(row-1,-1,-1):#other direction
            sums += input[r][column]
            dist.append(input[r][column-1]+sums)
        col[row] = min(dist)
    for row in xrange(0,dim):
        input[row][column] += col[row]
    
min = 9999999999999
for r in input:
    if r[dim-1] < min:
        min = r[dim-1]

print min
