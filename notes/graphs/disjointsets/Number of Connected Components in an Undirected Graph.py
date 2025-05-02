class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        setx = self.find(x)
        sety =self.find(y)
        if self.rank[setx] > self.rank[sety]:
            self.parent[sety] = setx
        elif self.rank[setx] < self.rank[sety]:
            self.parent[setx] = sety
        else:
            self.parent[sety] = setx
            self.rank[setx] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edges_compile = UnionFind(n)
        for edge in edges:
            x, y = edge
            edges_compile.union(x, y)
        components = [edges_compile.find(i) for i in range(n)]
        return len(set(edges_compile.parent))


