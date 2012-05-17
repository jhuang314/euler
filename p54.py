#problem 54

'''
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
'''

def classify(hand):
    handv = []
    for card in hand:
        if card[0].isdigit():
            handv.append(int(card[0]))
        else:
            if card[0] == "T":
                handv.append(10)
            if card[0] == "J":
                handv.append(11)
            if card[0] == "Q":
                handv.append(12)
            if card[0] == "K":
                handv.append(13)
            if card[0] == "A":
                handv.append(14)
    handv.sort()

    divide = 0
    while hand[divide][0].isdigit() and divide < 4:
        divide += 1

    isStrait = True
    for i in xrange(0,4):
        if handv[i]+(4-i) != handv[4]:
            isStrait = False
    isFlush = True
    for i in xrange(0,5):
        if hand[i][1] != hand[4][1]:
            isFlush = False


    match = False
    pairs = []
    for i in xrange(0,5):
        for pair in pairs:
            if handv[i] in pair:
                pair.append(handv[i])
                match = True
        if match:
            match = False
        else:
            pairs.append([handv[i]])
    
    isThree = False
    isTwoTwo = False
    isTwo = False
    maxv = 0
    maxvP = 0 #first max pair
    maxvPP = 0 #second max pair
    for pair in pairs:
        if len(pair) == 4:
            return (8,pair[0],max(handv)) #4 of a kind
        if len(pair) == 3:
            isThree = True
            if pair[0] > maxv:
                maxv = pair[0]
        if len(pair) == 2:
            if isTwo == True:
                isTwoTwo = True
            isTwo = True
            if pair[0] > maxvP:
                if maxvP > 0: maxvPP = maxvP
                maxvP = pair[0]


    if isFlush and isStrait:
        cardv = [s[0] for s in hand]
        if 'T' in cardv and 'J' in cardv and 'Q' in cardv and 'K' in cardv and 'A' in cardv:
            return (10,14,14) #royal flush
        return (9,max(handv),max(handv)) #strait flush

    if isThree and isTwo:
        return (7, maxv,maxvP,max(handv)) #full house

    if isFlush: return (6,max(handv)) #flush
    if isStrait: return (5,max(handv)) #strait 


    if isThree: return (4,maxv,max(handv)) #3 of a kind
    if isTwoTwo:
        return (3,maxvP,maxvPP,max(handv)) #2 pairs
    if isTwo:
        return (2,maxvP,max(handv)) #1 pair
    return (1,max(handv)) #highest card


count = 0
for i in xrange(0,1000):
    row = raw_input().strip().split(' ')
    p1 = row[:5]
    p2 = row[5:]
    p1.sort()
    p2.sort()
    p1c = classify(p1)
    p2c = classify(p2)
    j = 0
    while p1c[j] == p2c[j]:
        j += 1
    if p1c[j] > p2c[j]:
        count += 1

print count
