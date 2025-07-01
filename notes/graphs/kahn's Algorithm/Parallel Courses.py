class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        num_semesters = 0

        adj = defaultdict(list)
        indegree = defaultdict(int)
        num_courses = 0

        for prev, nxt in relations:
            adj[prev].append(nxt)
            indegree[nxt] += 1

        queue = deque([course for course in range(1, n+1) if course not in indegree ])

        if len(queue) == 0:
            return -1

        while queue:
            num_semesters += 1
            current_semester = len(queue)
            for _ in range(current_semester):
                current_course = queue.popleft()
                num_courses += 1
                if current_course in adj:
                    for nei in adj[current_course]:
                        indegree[nei] -= 1
                        if indegree[nei] == 0:
                            queue.append(nei)

        return num_semesters if num_courses == n else -1