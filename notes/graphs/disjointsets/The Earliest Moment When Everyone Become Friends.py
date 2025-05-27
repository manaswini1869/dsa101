class UnionFind:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        setx = self.find(x)
        sety = self.find(y)
        if self.rank[setx] > self.rank[sety]:
            self.parent[sety] = setx
        elif self.rank[setx] < self.rank[sety]:
            self.parent[setx] = sety
        else:
            self.parent[sety] = setx
            self.rank[setx] += 1




class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        earliest = float('inf')
        logs = sorted(logs)
        numberOfComponents = n
        for log in logs:
            timestamp, x, y = log
            if uf.find(x) != uf.find(y):
                numberOfComponents -= 1
                uf.union(x, y)
            if numberOfComponents == 1:
                earliest = min(timestamp, earliest)
        return -1 if numberOfComponents > 1 else earliest