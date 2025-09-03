class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def calculate_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n, m = len(workers), len(bikes)
        res = 0

        dist = [[calculate_distance(workers[i], bikes[j]) for j in range(m)] for i in range(n)]

        @lru_cache(None)
        def dp(worker_idx, mask):
            if worker_idx == n:
                return 0

            min_total = float('inf')
            for bike_idx in range(m):
                if not (mask & (1 << bike_idx)):
                    min_total = min(min_total, dist[worker_idx][bike_idx] + dp(worker_idx + 1, mask | (1 << bike_idx)))
            return min_total

        return dp(0, 0)

