#problem 6

def sumsq(x):
    return x*(x+1)*(2*x+1) / 6

def sqsum(x):
    return pow(x*(x+1)/2, 2)

print sqsum(100)-sumsq(100)
