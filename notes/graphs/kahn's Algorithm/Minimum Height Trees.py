class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]
        adj = defaultdict(list)
        res = []
        indegree = defaultdict(int)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        queue = deque([k for k, v in indegree.items() if v == 1])
        while n > 2:
            curr = len(queue)
            n -= curr
            for i in range(curr):
                left = queue.popleft()
                for nei in adj[left]:
                    indegree[nei] -= 1

                    if indegree[nei] == 1:
                        queue.append(nei)

        return list(queue)




