class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        n = len(s)
        if n < 2:
            return n
        seen = set()
        max_len = float("-inf")

        for right in range(n):
            while seen and s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len






