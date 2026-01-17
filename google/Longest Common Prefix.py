class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        strs.sort()
        ans = strs[0]

        for s in strs[1:]:
            n = min(len(s), len(ans))
            i = 0
            while i < n and s[i] == ans[i]:
                i += 1
            ans = ans[:i]
            if not ans:
                break

        return ans






