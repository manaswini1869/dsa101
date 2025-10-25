class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for i in range(rows):
            for j in range(cols-2, -1, -1):
                if boxGrid[i][j] == '#':
                    k = j
                    while k + 1 < cols and boxGrid[i][k+1] == '.':
                        boxGrid[i][k], boxGrid[i][k+1] = boxGrid[i][k+1], boxGrid[i][k]
                        k += 1

        output = [["."] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                output[j][rows - i - 1] = boxGrid[i][j]

        return output
