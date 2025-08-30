class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        # checking rows
        for i in range(rows):
            row = set()
            for j in range(cols):
                if board[i][j] in row:
                    return False
                else:
                    if board[i][j] != ".":
                        row.add(board[i][j])

        # column verification
        for i in range(rows):
            col = set()
            for j in range(cols):
                if board[j][i] in col:
                    return False
                else:
                    if board[j][i] != ".":
                        col.add(board[j][i])

        # square verification
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = set()
                for r in range(3):
                    for c in range(3):
                        if board[i + r][j + c] in box:
                            return False
                        else:
                            if board[i + r][j + c] != ".":
                                box.add(board[i + r][j + c])

        return True