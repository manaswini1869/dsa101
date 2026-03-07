from collections import defaultdict
from typing import List

class Cell:
    def __init__(self):
        self.val = 0
        self.formula = defaultdict(int)  # cells this cell depends on

class Excel:

    def __init__(self, height: int, width: str):
        w = ord(width) - ord('A') + 1
        self.mat = [[Cell() for _ in range(w)] for _ in range(height)]
        self.dependents = defaultdict(set)  # reverse dependency graph

    def set(self, row: int, column: str, val: int) -> None:
        r = row - 1
        c = ord(column) - ord('A')
        cell = self.mat[r][c]

        # remove old dependencies
        for (rr, cc) in cell.formula:
            self.dependents[(rr, cc)].discard((r, c))

        cell.formula.clear()

        diff = val - cell.val
        cell.val = val

        self._propagate(r, c, diff)

    def get(self, row: int, column: str) -> int:
        return self.mat[row-1][ord(column)-ord('A')].val

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        r = row - 1
        c = ord(column) - ord('A')
        cell = self.mat[r][c]

        # remove previous dependencies
        for (rr, cc) in cell.formula:
            self.dependents[(rr, cc)].discard((r, c))

        cell.formula.clear()

        for num in numbers:

            if ":" not in num:
                rr = int(num[1:]) - 1
                cc = ord(num[0]) - ord('A')
                cell.formula[(rr, cc)] += 1
                self.dependents[(rr, cc)].add((r, c))

            else:
                start, end = num.split(":")
                r1, c1 = int(start[1:]) - 1, ord(start[0]) - ord('A')
                r2, c2 = int(end[1:]) - 1, ord(end[0]) - ord('A')

                for i in range(r1, r2+1):
                    for j in range(c1, c2+1):
                        cell.formula[(i, j)] += 1
                        self.dependents[(i, j)].add((r, c))

        new_val = 0
        for (rr, cc), count in cell.formula.items():
            new_val += self.mat[rr][cc].val * count

        diff = new_val - cell.val
        cell.val = new_val

        self._propagate(r, c, diff)

        return cell.val

    def _propagate(self, r, c, diff):
        for (rr, cc) in self.dependents[(r, c)]:
            dependent_cell = self.mat[rr][cc]

            multiplier = dependent_cell.formula[(r, c)]
            delta = diff * multiplier

            dependent_cell.val += delta

            self._propagate(rr, cc, delta)