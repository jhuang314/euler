#problem 79
import string

#grab input from keylog.txt, and create a list
input = []

for i in range(50):
    a = raw_input().strip()
    if a not in input:
        input.append(a)

#from list, create graph
graph = {}
for i in input:
    if i[0] not in graph:
        graph[i[0]] = []
    if i[1] not in graph[i[0]]: #avoid duplicates
        graph[i[0]].append(i[1])
    if i[1] not in graph:
        graph[i[1]] = []
    if i[2] not in graph[i[1]]: #avoid duplicates
        graph[i[1]].append((i[2]))

graph['0'] = []

#get topological sort (via dfs)
postvisit = []
visited = {}


for vertex in graph:
    visited[vertex] = False

def explore(vertex):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            explore(neighbor)
    postvisit.insert(0,vertex)

for vertex in graph:
    if not visited[vertex]:
        explore(vertex)

password = ''
for v in postvisit:
    password += v
print password
