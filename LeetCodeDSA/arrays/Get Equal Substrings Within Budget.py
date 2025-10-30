class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        s = list(s)
        t = list(t)

        curr_cost = 0
        curr_len = 0
        max_len = 0
        left = 0

        for right in range(n):
            curr_cost += abs(ord(s[right]) - ord(t[right]))

            while curr_cost > maxCost and left <= right:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len



