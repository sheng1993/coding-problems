class DisjointSet():
    def __init__(self, size: int):
        self.size = size
        self.parent = [-1] * self.size
        self.rank = [0] * self.size
        self.makeSet()
    
    def makeSet(self):
        for i in range(self.size):
            self.parent[i] = i

    def find(x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(x: int, y: int):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1