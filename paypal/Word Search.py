class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return False

        rows, cols = len(board), len(board[0])
        visit = set()
        n = len(word)

        def dfs(r, c, i):
            if i == n:
                return True
            if r >= rows or c >= cols  or r < 0 or c < 0 or board[r][c] != word[i] or (r, c) in visit:
                return False

            visit.add((r, c))
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            visit.remove((r, c))
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False