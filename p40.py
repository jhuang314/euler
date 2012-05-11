#problem 40

num = '.'
for i in range(1,3000000):
    num += str(i)

print num[1],num[10],num[100],num[1000],num[10000],num[100000],num[1000000]
total = int(num[1])*int(num[10])*int(num[100])*int(num[1000])*int(num[10000])*int(num[100000])*int(num[1000000])
print total
