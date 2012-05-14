#problem 56

d = 0L
max = 0
for a in range(1,100):
    for b in range(1,100):
        d = a**b
        dstr = str(d)
        sum = 0
        for c in dstr:
            sum += int(c)
        if max < sum:
            max = sum
print max
