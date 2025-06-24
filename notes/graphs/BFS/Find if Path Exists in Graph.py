class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)

        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        seen = set()
        queue = deque([source])
        seen.add(source)

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for nei in adj_list[node]:
                if nei not in seen:
                    queue.append(nei)
                    seen.add(nei)

        return False


