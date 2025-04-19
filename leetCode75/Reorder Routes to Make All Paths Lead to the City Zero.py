class Solution:
    def __init__(self):
        self.count = 0
    def dfs(self, node, parent, adj):
        for neighbor, direction in adj[node]:
            if neighbor == parent:
                continue
            if direction == 1:
                self.count += 1
            self.dfs(neighbor, node, adj)


    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append((connection[1], 1))
            adj[connection[1]].append((connection[0], 0))
        self.dfs(0,-1,adj)
        return self.count