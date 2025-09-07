class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_matrix = collections.defaultdict(list)

        for u, v, t in times:
            adj_matrix[u].append((v, t))

        q = deque([(k, 0)])

        time = 0
        dist = {node: float('inf') for node in range(1, n+1)}
        dist[k] = 0
        while q:
            curr, tim = q.popleft()
            if dist[curr] < tim:
                continue
            for nei, w in adj_matrix[curr]:
                if tim + w < dist[nei]:
                    dist[nei] = tim + w
                    q.append((nei, tim+w))
        res = max(dist.values())
        return res if res < float('inf') else -1
