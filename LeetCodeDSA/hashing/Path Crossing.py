class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        start = [0, 0]

        move = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}

        for pa in path:
            start[0] += move[pa][0]
            start[1] += move[pa][1]
            print(start)
            if tuple(start) in visited:
                return True
            visited.add(tuple(start))

        return False
