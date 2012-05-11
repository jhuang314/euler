#problem 42

d = {}
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 1
for c in alpha:
    d[c]=i
    i += 1

def score(word):
    score = 0
    for c in word:
        score += d[c]
    return score

triangle = []
for i in range(1,40):
    triangle.append(i*(i+1)/2)

s = raw_input().split(",")

count = 0
for word in s:
    word = word[1:-1]
    scr = score(word)
    if scr in triangle:
        count += 1

print count
