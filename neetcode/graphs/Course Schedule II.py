class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            courses[course].append(prereq)

        res = []
        visit_set, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit_set:
                return True

            cycle.add(course)
            for pre in courses[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit_set.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
