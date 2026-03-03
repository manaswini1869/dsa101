class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if not edges:
            return 0

        adj_matrix = defaultdict(list)

        for x, y in edges:
            adj_matrix[x].append(y)
            adj_matrix[y].append(x)

        visit = set()

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj_matrix[node]:
                if nei not in visit:
                    dfs(nei)
        no_connected = 0
        for i in range(n):
            if i not in visit:
                no_connected += 1
                dfs(i)

        return no_connected





