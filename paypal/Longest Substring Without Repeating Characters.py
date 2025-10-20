class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        vis = set()
        res = len(vis)

        n = len(s)

        for right in range(n):
            while s[right] in vis:
                vis.remove(s[left])
                left += 1
            vis.add(s[right])
            res = max(res, right - left + 1)
        return res



