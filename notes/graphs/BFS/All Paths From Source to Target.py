class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        seen = set()

        adj_list = defaultdict(list)
        n = len(graph)
        for i in range(n):
            adj_list[i] = graph[i]
        destination = n - 1
        queue = deque([[0]])
        while queue:

            current_path = queue.popleft()
            last_node = current_path[-1]

            if last_node == destination:
                result.append(current_path)
                continue

            for nei in adj_list[last_node]:
                new_path = current_path[:]
                new_path.append(nei)
                queue.append(new_path)


        return result

