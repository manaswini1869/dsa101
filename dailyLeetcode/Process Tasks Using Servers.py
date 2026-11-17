class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        n = len(servers)
        m = len(tasks)

        if m == 0:
            return []

        ans = []

        servers = [[num, idx] for idx, num in enumerate(servers)]

        heapq.heapify(servers)

        q = []
        t = 0

        for i in range(m):
            t = max(t, i)
            while q and q[0][0] <= t:
                fin, server, idx = heapq.heappop(q)
                heapq.heappush(servers, [server, idx])

            if not servers:
                t = q[0][0]
                while q and q[0][0] <= t:
                    fin, server, idx = heapq.heappop(q)
                    heapq.heappush(servers, [server, idx])

            server, idx = heapq.heappop(servers)
            ans.append(idx)
            heapq.heappush(q, [t+tasks[i], server, idx])


        return ans