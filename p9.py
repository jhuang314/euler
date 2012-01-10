#problem 9

def isTriplet(t):
    if pow(t[0],2)+pow(t[1],2) == pow(t[2],2):
        return True
    return False

for a in range(1,1000):
    for b in range(1,1000-a):
        c = 1000 - a - b
        if isTriplet([a,b,c]):
            print [a,b,c]
            print a*b*c

