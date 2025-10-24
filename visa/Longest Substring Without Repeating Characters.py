class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) <= 2:
            return len(set(s))

        ans = 0
        visit = set()
        left = 0
        visit.add(s[left])
        n = len(s)
        for right in range(1, n):
            while s[right] in visit:
                visit.remove(s[left])
                left += 1

            ans = max(ans, right - left + 1)
            visit.add(s[right])

        return ans
