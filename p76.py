#problem 76

target = 100
coins = [x for x in range(1,target)]
ways = [1]+[0]*target

for coin in coins:
  for i in range(coin, target+1):
    ways[i] += ways[i-coin]
 
print ways[target]

