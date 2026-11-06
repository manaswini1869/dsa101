class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        arr = [0] * len(queries)
        logs = sorted(logs, key=lambda x: x[1])
        queries = sorted((q, i) for i, q in enumerate(queries))
        servers = {}
        log_n = len(logs)
        left = right = 0

        for query, idx in queries:
            x1, x2 = query - x, query
            while right < log_n and logs[right][1] <= x2:
                server = logs[right][0]
                servers[server] = servers.get(server, 0)+1
                right += 1

            while left < right and logs[left][1] < x1:
                server = logs[left][0]
                servers[server] -= 1

                if servers[server] == 0:
                    del servers[server]

                left += 1

            arr[idx] = n - len(servers)

        return arr