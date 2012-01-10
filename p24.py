#problem 24
from math import factorial
'''
digits = ["0","1","2","3","4","5","6","7","8","9"]

x = 1000000
out = ""
for i in range(0,10):
    out += digits[int(x / factorial(9-i))]
    x = x - int(out) * factorial(9-i)
    print out
    
print out
'''

def p(x):
    digits = [0,1,2,3,4,5,6,7,8,9]
    
    out = ""
    for i in range(0,10):
        v = x / factorial(9-i)
#        print "v is:",v, "x is:", x
        temp = digits[v]
        digits.remove(temp)
        out += str(temp)
        x = x - v * factorial(9-i)

    print out
p(1000000)




