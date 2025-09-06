class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0

        adj_matrix = [[] for _ in range(n)]

        for a, b in edges:
            adj_matrix[a].append(b)
            adj_matrix[b].append(a)

        visit_set = set()
        def dfs(node):
            if node in visit_set:
                return

            visit_set.add(node)
            for nei in adj_matrix[node]:
                dfs(nei)

        for i in range(n):
            if i not in visit_set:
                dfs(i)
                count += 1

        return count

