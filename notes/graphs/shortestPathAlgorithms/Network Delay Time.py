class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n == 0:
            return -1

        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        distance = {i: float('inf') for i in range(1, n+1)}
        distance[k] = 0

        max_time = [(k, 0)]

        while max_time:
            u, weight = heapq.heappop(max_time)

            if weight > distance[u]:
                continue

            for v, w in adj[u]:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    heapq.heappush(max_time, (v, distance[v]))

        res = 0

        for i in range(1, n+1):
            if distance[i] == float('inf'):
                return -1

            res = max(res, distance[i])

        return res


