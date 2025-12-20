class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        rows, cols = len(strs), len(strs[0])

        no_deletions = 0

        for i in range(cols):
            for j in range(1, rows):
                if strs[j-1][i] > strs[j][i]:
                    no_deletions += 1
                    break


        return no_deletions




