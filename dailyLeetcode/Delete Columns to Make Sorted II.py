class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        no_deletions = 0
        rows, cols = len(strs), len(strs[0])
        sorted_pairs = [False]*(rows-1)

        for c in range(cols):
            for r in range(rows-1):
                if not sorted_pairs[r] and strs[r][c] > strs[r+1][c]:
                    no_deletions += 1
                    break
            else:
                for r in range(rows-1):
                    if not sorted_pairs[r] and strs[r][c] < strs[r+1][c]:
                        sorted_pairs[r] = True


        return no_deletions







