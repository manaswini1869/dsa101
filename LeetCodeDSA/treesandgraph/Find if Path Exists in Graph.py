class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        if not edges:
            return False

        adj_matrix = defaultdict(list)

        for x, y in edges:
            adj_matrix[x].append(y)
            adj_matrix[y].append(x)

        visit = set()

        def dfs(node):
            if node == destination:
                return True

            visit.add(node)

            for nei in adj_matrix[node]:
                if nei not in visit:
                    if dfs(nei):
                        return True

            return False


        return dfs(source)








