class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        setx = self.find(x)
        sety = self.find(y)
        if setx == sety:
            return False
        if self.rank[setx] < self.rank[sety]:
            self.parent[setx] = sety
        elif self.rank[setx] > self.rank[sety]:
            self.parent[sety] = setx
        else:
            self.parent[sety] = setx
            self.rank[setx] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        uf = UnionFind(n)
        for x,y in edges:
            if not uf.union(x, y):
                return False
        return True

