class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        heap = [(0, s)]
        distances = {i: float('inf') for i in range(n)}
        distances[s] = 0
        visited = set()

        while heap:
            curr_dist, node = heapq.heappop(heap)

            if node in marked:
                return curr_dist
            if node in visited:
                continue
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    new_dist = curr_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))

        return -1