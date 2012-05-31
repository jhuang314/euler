#dijkstras

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

#testing the algorithm
G['a']=['b','c','d']
G['b'] = ['c']
G['c'] = []
G['d'] = []

E[('a','b')] = 1
E[('a','c')] = 100
E[('a','d')] = 1
E[('b','c')] = 1

V = ['a','b','c','d']
print dijkstras('a')
