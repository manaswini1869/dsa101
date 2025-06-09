class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        seen = set()
        path = [source]
        while path:
            node = path.pop()
            if node == destination:
                return True
            if node in seen:
                continue
            seen.add(node)
            for neig in adj[node]:
                path.append(neig)
        return False