class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_matrix = [[] for _ in range(n+1)]

        def dfs(node, par):
            if visit[node]:
                return True

            visit[node] = True
            for nei in adj_matrix[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False

        for a, b in edges:
            adj_matrix[a].append(b)
            adj_matrix[b].append(a)
            visit = [False] * (n+1)

            if dfs(a, -1):
                return [a, b]
        return []