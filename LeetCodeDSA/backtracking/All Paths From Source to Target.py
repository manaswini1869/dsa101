class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph)
        adj = defaultdict(list)
        for i in range(n):
            adj[i] = graph[i]

        def dfs(node, curr):
            if node == n-1:
                answer.append(curr[:])
                return
            for nei in adj[node]:
                curr.append(nei)
                dfs(nei, curr)
                curr.pop()


        answer = []
        dfs(0, [0])


        return answer





