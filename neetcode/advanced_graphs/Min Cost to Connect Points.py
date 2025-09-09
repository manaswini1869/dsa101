class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj = {i: [] for i in range(n)}

        # edge portion
        for i in range(n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # prim's
        res = 0
        visit = set()
        min_h = [[0, 0]] # cost, node

        while len(visit) < n:
            cost, i = heapq.heappop(min_h)
            if i in visit:
                continue

            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(min_h, [neiCost, nei])

        return res


