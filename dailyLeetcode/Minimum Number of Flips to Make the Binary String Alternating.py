class Solution:
    def minFlips(self, s: str) -> int:

        target = "01"
        n = len(s)

        mismatch = sum(char != target[i&1] for i, char in enumerate(s))

        min_flips = min(mismatch, n - mismatch)

        for i in range(n):
            mismatch -= s[i] != target[i&1]
            mismatch += s[i] != target[(i+n)&1]
            min_flips = min(min_flips, mismatch, n - mismatch)


        return min_flips

        # time complexity = O(n)
        # space complexity = O(1)


        