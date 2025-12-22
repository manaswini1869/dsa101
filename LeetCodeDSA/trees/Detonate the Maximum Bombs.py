class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        n = len(bombs)
        adj_matrix = [[] for _ in range(n)]


        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                if (x1 - x2)**2 + (y1-y2)**2 <= r1**2:
                    adj_matrix[i].append(j)

        def dfs(start):
            stack = [start]
            seen = set([start])
            while stack:
                node = stack.pop()
                for nei in adj_matrix[node]:
                    if nei in seen:
                        continue
                    stack.append(nei)
                    seen.add(nei)
            return len(seen)

        return max(dfs(i) for i in range(n))





