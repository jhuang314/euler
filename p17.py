#problem 17

ones = dict({1:"one", 2:"two", 3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine", 10:"ten"})
tens = dict({11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"})

def ten(x):
    if x <= 10:
        return ones[x]
    if x < 20 and x > 10:
        return tens[x]
    else:
        ten = x - x%10
        if x%10 not in ones:
            one = ""
        else:
            one = ones[x%10]
        return tens[ten]+one


def hundreds(x):
    h = (x - x%100) / 100
    out = ones[h] + "hundred"
    if (x - h * 100) != 0:
        out += "and"
        out += ten(x - h * 100)
    return out

mess = ""
for i in range(1,100):
    mess += ten(i)

for i in range(100, 1000):
    mess += hundreds(i)
mess += "onethousand"


print len(mess)
    
    
