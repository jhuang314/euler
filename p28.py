#solution for problem 28

sum = 1  #keeps track of sum
gap = 2  #keeps track of gap between edges of spiral
col = 1  #keeps track of size of spiral (from middle to one end)
value = 1 #keeps track of the upper right most diagonal value

while col <= 500:

    sum = sum + value * 4 + gap * 10
    '''
    sum = sum + value + gap
    sum = sum + value + gap * 2
    sum = sum + value + gap * 3
    value = value + gap * 4
    sum = sum + value
    '''

    value = value + gap * 4

    gap = gap + 2
    col = col + 1

print sum

