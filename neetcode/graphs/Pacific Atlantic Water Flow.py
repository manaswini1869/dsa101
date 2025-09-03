class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows, cols = len(heights), len(heights[0])
        pacific = []
        atlantic = []
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    pacific.append((i, j))
                if i == rows - 1 or j == cols - 1:
                    atlantic.append((i, j))
        def bfs(curr):
            # base case: check if the co-ordinate reached opposite
            q = deque(curr)
            visit = set(curr)

            while q:
                x, y = q.popleft()
                val = heights[x][y]
                for dx, dy in directions:
                    if 0 <= x + dx < rows and 0 <= y+dy < cols and ((x + dx, y+dy) not in visit) and (heights[x+dx][y+dy] >= val):
                        q.append((x+dx, y+dy))
                        visit.add((x+dx, y+dy))

            return visit

        pacific_reach = bfs(pacific)
        atlantic_reach = bfs(atlantic)

        res = list(map(list, pacific_reach & atlantic_reach))

        return res