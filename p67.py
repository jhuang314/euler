#problem 67

#Grab input from text
triangle = []

for j in range(0,100):
    r = raw_input().strip().split(" ")
    ri = []
    for x in r:
        ri.append(int(x))
    triangle.append(ri)


#Use dynamic programming
C = [triangle[0]]

last = len(triangle)
for row in range(1,last):
    C.append([])
    for col in range(0,row+1):
        if col == 0:
            C[row].append(C[row-1][col]+triangle[row][col])         
        elif col == row:
            C[row].append(C[row-1][col-1]+triangle[row][col])         
        else:
            C[row].append(max([C[row-1][col],C[row-1][col-1]])+triangle[row][col])

print max(C[last-1])
