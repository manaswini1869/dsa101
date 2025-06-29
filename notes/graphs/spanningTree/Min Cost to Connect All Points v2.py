class Edge:
    def __init__(self, p1, p2, cost):
        self.p1 = p1
        self.p2 = p2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if not points or n == 0:
            return 0

        visited = [False] * n
        edges = []
        res = 0

        for i in range(1, n):
            cost = abs(points[0][0] - points[i][0])+abs(points[0][1] - points[i][1])
            edge = Edge(0, i, cost)
            edges.append(edge)

        count = n - 1
        heapq.heapify(edges)

        visited[0] = True

        while edges and count > 0:
            edge = heapq.heappop(edges)
            p1 = edge.p1
            p2 = edge.p2
            cost = edge.cost
            if not visited[p2]:
                res += cost
                visited[p2] = True
                for j in range(n):
                    if not visited[j]:
                        distance = abs(points[j][0] - points[p2][0]) + abs(points[j][1] - points[p2][1])
                        heapq.heappush(edges, Edge(p2, j, distance))

                count -= 1




        return res
