
class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
        self.count = [1]*N

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, s1, s2):
        par1, par2 = self.find(s1), self.find(s2)
        if par1 == par2:
            return False
        if self.count[par1] < self.count[par2]:
            self.count[par1], self.count[par2] = self.count[par2], self.count[par1]
        self.parent[par2] = par1
        self.count[par1] += self.count[par2]
        self.count[par2] = self.count[par1]
        return True


