class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[src] = 0
        for _ in range(k+1):
            tmp_cost = list(costs)
            for fromi, toi, pricei in flights:
                if costs[fromi] != float('inf'):
                    tmp_cost[toi] = min(tmp_cost[toi], costs[fromi] + pricei)
            costs = tmp_cost

        return costs[dst] if costs[dst] != float('inf') else -1
#         res = 0
#         adj = defaultdict(list)
#         for u, v, w in flights:
#             adj[u].append((v, w))

#         costs = {}

#         for i in range(n):
#             costs[i] = {}
#             for j in range(k + 2):
#                 costs[i][j] = float('inf')

#         costs[src][0] = 0

#         min_cost = [(0, src, 0)]

#         while min_cost:
#             w, u, stops = heapq.heappop(min_cost)

#             if w > costs[u].get(stops, float('inf')) or stops > k + 1:
#                 continue

#             for v, weight in adj[u]:
#                 new_stops = stops + 1
#                 if new_stops <= k + 1 and w + weight < costs[v].get(new_stops, float('inf')):
#                     costs[v][new_stops] = w + weight
#                     heapq.heappush(min_cost, (w + weight, v, new_stops))

#         res = float('inf')

#         for stop in range(k + 2):
#             res = min(res, costs[dst].get(stop, float('inf')))

#         return res if res != float('inf') else -1