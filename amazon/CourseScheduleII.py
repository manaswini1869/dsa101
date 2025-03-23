class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for pre_req in prerequisites:
            adj[pre_req[1]].append(pre_req[0])
            indegree[pre_req[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        node_visited = []
        while queue:
            node = queue.popleft()
            node_visited.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return node_visited if len(node_visited) == numCourses else []
