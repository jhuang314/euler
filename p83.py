#problem 83

G = {}
E = {}
V = []
inf = float('inf')

def insert(e):
    if e[0] not in G:
        G[e[0]] = [e[1]]
    else:
        G[e[0]].append(e[1])
    

def dijkstras(s):
    dist = {}
    prev = {}
    q = {}
    if s not in V:
        return "OOPS"
    for v in V:
        dist[v] = inf
        prev[v] = None
        q[v] = inf
    dist[s] = 0
    q[s] = 0
    prev[s] = None
    while len(q) > 0:
        key = min(q)
        v = q[key]
        del q[key]
        for neighbor in G[key]:
            weight = v+E[(key,neighbor)]
            if weight < dist[neighbor]:
                dist[neighbor] = weight
                q[neighbor] = weight
                prev[neighbor] = key
    return (dist,prev)


input = []
for i in xrange(0,80):
    input.append([int(x) for x in raw_input().strip().split(',')])

dim = len(input)
    
#build graph
for i in xrange(0,dim):
    for j in xrange(0,dim-1):
        x1 = 'x' + str(j) + 'y' + str(i)
        x2 = 'x' + str(j+1) + 'y' + str(i)
        insert((x1,x2))
        insert((x2,x1))
        E[(x1,x2)] = input[i][j+1]
        E[(x2,x1)] = input[i][j]

for i in xrange(0,dim-1):
    for j in xrange(0,dim):
        x1 = 'x' + str(j) + 'y' + str(i)
        x2 = 'x' + str(j) + 'y' + str(i+1)
        insert((x1,x2))
        insert((x2,x1))
        E[(x1,x2)] = input[i+1][j]
        E[(x2,x1)] = input[i][j]

for i in xrange(0,dim):
    for j in xrange(0,dim):
        x1 = 'x' + str(j) + 'y' + str(i)
        V.append(x1)

res = dijkstras('x0y0')
print res[0]['x79y79']+input[0][0]

