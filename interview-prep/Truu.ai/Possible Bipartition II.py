class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_matrix = {i:[] for i in range(1, n+2)}
        groups = {}
        for a, b in dislikes:
            adj_matrix[a].append(b)
            adj_matrix[b].append(a)
        for node in range(1, n+1):
            if node not in groups:
                groups[node] = 0
                stack = [node]
                while stack:
                    curr = stack.pop()
                    for nei in adj_matrix[curr]:
                        if nei not in groups:
                            groups[nei] = 1 - groups[curr]
                            stack.append(nei)
                        elif groups[nei] == groups[curr]:
                            return False
        return True