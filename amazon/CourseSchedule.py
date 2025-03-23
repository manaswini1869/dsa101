class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for pre_req in prerequisites:
            adj[pre_req[1]].append(pre_req[0])
            indegree[pre_req[0]] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        nodes_visited = 0
        while queue:
            node = queue.popleft()
            nodes_visited += 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return nodes_visited == numCourses