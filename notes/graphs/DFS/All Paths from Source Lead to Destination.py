class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for sour, desti in edges:
            adj_list[sour].append(desti)
        visited = {}

        def dfs(node):
            if node not in adj_list:
                return node == destination
            if node in visited:
                return visited[node] == 2
            visited[node] = 1
            for nei in adj_list[node]:
                if not dfs(nei):
                    return False
            visited[node] = 2
            return True

        return dfs(source)
