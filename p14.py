#problem 14

def collatz(x):
    sum = 1
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        sum += 1
    return sum


maxlength = 0
value = 0
for i in range(1,1000000):
    length = collatz(i)
    if length > maxlength:
        maxlength = length
        value = i

print value
print maxlength

