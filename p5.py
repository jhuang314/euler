# Problem 5 solution

def div(x):
    if x % 16 == 0 and x % 3 == 0 and x % 5 == 0 and x % 7 == 0 and x % 11 == 0 and x % 13 == 0 and x % 17 == 0 and x % 19 == 0 and x % 18 == 0 and x % 20 == 0:
        return True
    return False

'''
just for testing stuff
def div2(x):
    if x % 16 == 0 and x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
        return True
    return False
'''

i = 20
while not div(i):
    i += 1

print i

