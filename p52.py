#problem 52

def checkEqual(iterator):
      try:
         iterator = iter(iterator)
         first = next(iterator)
         return all(first == rest for rest in iterator)
      except StopIteration:
         return True

def check(x):
    l = [y for y in range(x,6*x+1,x)]

    a = [list(str(y)) for y in l]
    for y in a:
        y.sort()
    b = [cat(y) for y in a]
    return checkEqual(b)

def cat(lst):
    res = ''
    for y in lst:
        res += y
    return int(res)

x = 1
while not check(x):
    x += 1
print x
