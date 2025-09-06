class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False

        adj_matrix = [[] for _ in range(n)]

        for a, b in edges:
            adj_matrix[a].append(b)
            adj_matrix[b].append(a)
        visit_set = set()

        def dfs(node, par):
            if node in visit_set:
                return False

            visit_set.add(node)
            for b in adj_matrix[node]:
                if b == par:
                    continue
                if not dfs(b, node):
                    return False
            return True

        return dfs(0, -1) and len(visit_set) == n