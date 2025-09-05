class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_matix = {i:[] for i in range(numCourses)}

        for cour, pre in prerequisites:
            adj_matix[cour].append(pre)

        visit_set = set()

        def dfs(crs):
            if crs in visit_set:
                return False
            if adj_matix[crs] == []:
                return True
            visit_set.add(crs)
            for pre in adj_matix[crs]:
                if not dfs(pre):
                    return False
            visit_set.remove(crs)
            adj_matix[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
