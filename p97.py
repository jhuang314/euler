#problem 97

digits = 1
for i in range(0,7830457):
    digits *= 2
    digits %= 10000000000

digits *= 28433
digits += 1
digits %= 10000000000

print digits
