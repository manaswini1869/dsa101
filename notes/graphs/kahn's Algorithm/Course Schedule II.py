class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        indegree = {}
        for cour, prereq in prerequisites:
            adj[prereq].append(cour)
            indegree[cour] = indegree.get(cour, 0) + 1

        queue = deque([k for k in range(numCourses) if k not in indegree])

        res = []
        while queue:
            vertex = queue.popleft()
            res.append(vertex)

            if vertex in adj:
                for nei in adj[vertex]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        queue.append(nei)

        return res if len(res) == numCourses else []
