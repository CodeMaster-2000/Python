class Graph:
    def __init__(self, n):
        self.n = n
        self.vertices = [[] for i in range(n)]
        self.inCut = [False for i in range(n)]
    
    def addEdge(self, u, v):
        self.vertices[u].append(v)
        self.vertices[v].append(u)
    
    def improvesCut(self, v):
        count = 0
        for neighbour in self.vertices[v]:
            if not self.inCut[neighbour]:
                count += 1
            else:
                count -= 1
        
        if not self.inCut[v]:
            return count > 0
        else:
            return count < 0
    
    def cutApprox(self):
        lastIteration = False
        while not lastIteration:
            lastIteration = True
            for v in range(self.n):
                if self.improvesCut(v):
                    lastIteration = False
                    self.inCut[v] = not self.inCut[v]
        count = 0
        S = []
        for v in range(self.n):
            if self.inCut[v]:
                S.append(v + 1)
                count += 1
        return count, S


n, m = map(int, input().split())

G = Graph(n)

for i in range(m):
    u, v = map(int, input().split())
    G.addEdge(u - 1, v - 1)

sizeS, S = G.cutApprox()
print(sizeS)
for v in S:
    print(f'{v} ', end = "")
print()
