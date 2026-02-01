class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        # dijstra's algorithm

        adj = [[] for _ in range(26)]
        count = len(original)
        for i in range(count):
            adj[ord(original[i]) - ord('a')].append((ord(changed[i]) - ord('a'), cost[i]))
        
        def short_cost(idx, matrix):
            heap = [(0, idx)]

            min_costs = [float("inf")]*26
            while heap:
                d, ch = heapq.heappop(heap)
                if d > min_costs[ch]:
                    continue
                min_costs[ch] = d
                for tch, conv in matrix[ch]:
                    new = d + conv
                    if min_costs[tch] > new:
                        min_costs[tch] = new
                        heapq.heappush(heap, (new, tch))
            
            return min_costs
            
        min_cost = [short_cost(i, adj) for i in range(26)]
        total = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            
            conv = min_cost[ord(s)-ord('a')][ord(t)-ord('a')]
            if conv == float("inf"):
                return -1
            total += conv
        return total



        # ans = 0
        # n = len(source)
        # arr_len = len(original)
        # adj_list = [[float("inf")]*26 for _ in range(26)]
        # for i in range(arr_len):
        #     u = ord(original[i])-ord('a')
        #     v = ord(changed[i])-ord('a')
        #     adj_list[u][v] = min(adj_list[u][v], cost[i])
        
        # for k in range(26):
        #     for i in range(26):
        #         for j in range(26):
        #             if adj_list[i][j] > adj_list[i][k] + adj_list[k][j]:
        #                 adj_list[i][j] = adj_list[i][k] + adj_list[k][j]
        
        # for src, dst in zip(source, target):
        #     if src == dst:
        #         continue
        #     s = ord(src) - ord('a')
        #     d = ord(dst) - ord('a')
        #     if adj_list[s][d] == float("inf"):
        #         return -1
        #     ans += adj_list[s][d]
        # return ans




        

        






        