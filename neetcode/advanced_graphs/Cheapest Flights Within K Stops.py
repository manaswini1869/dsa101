class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}

        for u, v, w in flights:
            adj[u].append((v, w))

        print(adj)

        cost = {}
        min_h = [(0, src, 0)]
        while min_h:
            cos, node, stops = heapq.heappop(min_h)
            if node == dst:
                return cos

            if stops <= k:
                for nei, co in adj[node]:
                    if (nei, stops) not in cost or co + cos < cost[(nei, stops)]:
                        heapq.heappush(min_h, (cos+co, nei, stops+1))

        return -1