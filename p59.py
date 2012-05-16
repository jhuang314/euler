#problem 59

def score(message):
    total = 0
    for c in message:
        total += ord(c)
    return total


def printMessage(array,key):
    message = ''
    for ascii in array:
        message += chr(ascii)
    if message.find("the") != -1 and message.find("this") != -1:
        print message,key,score(message)


def decrypt(array, key):
    index = 0
    decrypted = []
    min = 128
    for ascii in array:
        char = ascii ^ key[index]
        if char < min: min = char
        decrypted.append(char)
        index += 1
        index %= 3
    return (decrypted,min)


raw = raw_input().strip().split(',')
encrypt = [int(x) for x in raw]

lower = 97
upper = 123
for a in xrange(lower,upper):
    for b in xrange(lower,upper):
        for c in xrange(lower,upper):
            res = decrypt(encrypt,[a,b,c])
            if res[1] >= 32:
                printMessage(res[0],[a,b,c])

