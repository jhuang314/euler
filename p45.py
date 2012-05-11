#problem 45

triangle = []
for i in range(1,400000,2):
    triangle.append(i*(i+1)/2)

pent = []
for j in range(1,1000000):
    pent.append(j*(3*j-1)/2)

i=0
j=0
count = 0
for k in range(0,3):
    while triangle[i]!=pent[j]:
        if triangle[i]<pent[j]:
            i += 1
        else:
            j += 1

    i += 1
    j += 1

print triangle[i-1]
