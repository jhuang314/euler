import math

def isPalindrome(x):
    string = str(x)
    start = 0
    end = len(string) - 1
    while end > start:
        if string[start] != string[end]:
            return False
        end -= 1
        start += 1
    return True

def search():
    candidates = []
    for a in range(800,1000):
        for b in range(800,1000):
            if isPalindrome(a*b):
                candidates += [a*b]
    print candidates
    print max(candidates)
search()
