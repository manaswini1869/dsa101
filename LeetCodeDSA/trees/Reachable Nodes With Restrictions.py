class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        visit = set()
        restricted = set(restricted)

        adj_matrix = defaultdict(list)

        for a, b in edges:
            adj_matrix[a].append(b)
            adj_matrix[b].append(a)


        def dfs(node):
            if node in visit or node in restricted:
                return
            visit.add(node)
            for nei in adj_matrix[node]:
                dfs(nei)



        dfs(0)



        return len(visit)







