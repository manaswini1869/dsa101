class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0 for _ in range(26)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:])-1
        self.sheet[row][col] = 0

    def _getCell(self, name):
        col = ord(name[0]) - ord('A')
        row = int(name[1:]) - 1  # 0-based row index
        return self.sheet[row][col]

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split('+')
        if x[0].isalpha():
            X = self._getCell(x)
        else:
            X = int(x)

        if y[0].isalpha():
            Y = self._getCell(y)
        else:
            Y = int(y)
        return X+Y





# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)