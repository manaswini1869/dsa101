class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for cou, pre in prerequisites:
            adj[cou].append(pre)

        for i in range(numCourses):
            stack = [(i, set())]

            while stack:
                curr, visited = stack.pop()
                if curr in visited:
                    return False
                visited.add(curr)
                for pre in adj[curr]:
                    stack.append((pre, visited.copy()))
            adj[i] = []

        return True


