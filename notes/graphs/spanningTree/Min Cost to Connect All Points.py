class Edge:
    def __init__(self, p1, p2, cost):
        self.p1 = p1
        self.p2 = p2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        selfX = self.find(x)
        selfY = self.find(y)

        if selfX != selfY:
            if self.rank[selfX] > self.rank[selfY]:
                self.root[selfY] = selfX
            elif self.rank[selfX] < self.rank[selfY]:
                self.root[selfX] = selfY
            else:
                self.root[selfX] = selfY
                self.rank[selfY] += 1
    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        count = n - 1
        if not points or n == 0:
            return 0

        edges = []
        res = 0
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edge = Edge(i, j, cost)
                edges.append(edge)

        heapq.heapify(edges)
        while edges and count > 0:
            edge = heapq.heappop(edges)

            if not uf.connected(edge.p1, edge.p2):
                uf.union(edge.p1, edge.p2)
                res += edge.cost
                count -= 1

        return res
