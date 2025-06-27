class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        current = 0
        power = 1

        n = len(s)

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                count += 1

            else:
                if current + power <= k:
                    current += power
                    count += 1
            if power > k :
                continue
            power *= 2
        return count


        return count