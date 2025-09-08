class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # hash_set so that we are not visiting the same node
        adj_matrix = {}
        for node in range(n):
        # check to make sure we are not visiting the same node
            if node not in adj_matrix:
                stack = [node]
                adj_matrix[node] = 0 # assign the node as 0 color
                while stack:
                    curr = stack.pop()
                    for v in graph[curr]: # looping its neighbors
                        if v not in adj_matrix:
                            adj_matrix[v] = 1 - adj_matrix[curr]
                            stack.append(v)
                        elif adj_matrix[v] == adj_matrix[curr]:
                            return False
        return True