class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        while x!= self.parent[x]:
            x = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        setx = self.find(x)
        sety = self.find(y)

        if self.rank[setx] > self.rank[sety]:
            self.parent[sety] = self.parent[setx]
        elif self.rank[setx] < self.rank[sety]:
            self.parent[setx] = self.parent[sety]
        else:
            self.parent[sety] = setx
            self.rank[setx] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        for pair in pairs:
            x, y = pair
            uf.union(x, y)

        groups = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)

        res = list(s)
        for indicies in groups.values():
            chars = [s[i] for i in indicies]
            indicies.sort()
            chars.sort()
            for i, ch in zip(indicies, chars):
                res[i] = ch

        return "".join(res)