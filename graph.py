#graph library and algorithms
#Jesse Huang
#5/18/2012

class Graph:
    def __init__(self):
        self.G = {}
        self.V = []
        self.E = []

    def addVertex(self,v):
        if v not in self.G:
            self.G[v] = []
            self.V.append(v)

    def addEdge(self,e):
        if len(e) == 2 and e not in self.E:
            if e[0] not in self.V:
                self.V.append(e[0])
                self.G[e[0]] = []
            if e[1] not in self.V:
                self.V.append(e[1])
                self.G[e[1]] = []
            self.E.append(e)
            self.G[e[0]].append(e[1])

    def removeEdge(self,e):
        if e in self.E:
            self.G[e[0]].remove(e[1])
            self.E.remove(e)


    def removeVertex(self,v):
        if v in self.V:
            self.V.remove(v)
            for vertex in self.G[v]:
                self.E.remove((v,vertex))
            del self.G[v]
            for vertex in self.G:
                if v in self.G[vertex]:
                    self.G[vertex].remove(v)
                    self.E.remove((vertex,v))

    def __str__(self):
        result = "Graph:\n"
        for node in self.G:
            result += str(node) + ":" + str(self.G[node]) + "\n"
        result += "Vertices:\n" + str(self.V) + "\nEdges:\n" + str(self.E)
        return result

    def explore(self, vertex):
        self.visited[vertex] = True
        pre = self.clock
        self.clock += 1
        for neighbor in self.G[vertex]:
            if not self.visited[neighbor]:
                self.explore(neighbor)
            else:
                if neighbor not in self.prepost:
                    self.hasCycle = True

        post = self.clock
        self.clock += 1
        self.prepost[vertex] = (pre,post)
        self.post.insert(0,vertex)

    def dfs(self):
        self.visited = {}
        self.prepost = {}
        self.post = []
        self.clock = 1
        self.hasCycle = False
        for vertex in self.V:
            self.visited[vertex] = False

        for vertex in self.V:
            if not self.visited[vertex]:
                self.explore(vertex)

        return self.prepost


    def isCyclic(self):
        self.dfs()
        return self.hasCycle

    def topsort(self):
        self.dfs()
        return self.post

    def reverse(self):
        rev = Graph()
        rev.V = self.V[:]
        for vertex in rev.V:
            rev.G[vertex] = []
        for edge in self.E:
            rev.E.append((edge[1],edge[0]))
            rev.G[edge[1]].append(edge[0])
        return rev

    def exploreSCC(self, vertex, lst):
        self.visited[vertex] = True
#        pre = self.clock
#        self.clock += 1
        for neighbor in self.G[vertex]:
            if not self.visited[neighbor]:
                lst.append(neighbor)
                lst = self.exploreSCC(neighbor,lst)
#            else:
#                if neighbor not in self.prepost:
#                    self.hasCycle = True

#        post = self.clock
#        self.clock += 1
#        self.prepost[vertex] = (pre,post)
#        self.post.insert(0,vertex)
        return lst


    def scc(self):
        reverse = self.reverse()
        reverse.dfs()

        scc = []
        lst = []
        self.visited = {}

        for vertex in reverse.post:
            self.visited[vertex] = False


        for vertex in reverse.post:
            if not self.visited[vertex]:
                print vertex
                scc.append(self.exploreSCC(vertex,lst))

        print scc
        #run modified dfs
        
        
x = Graph()
x.addEdge((1,2))
x.addEdge((2,3))
x.addEdge((3,1))
x.addEdge((3,4))


x.scc()

