class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            curr = ""
            for idx in range(0, len(s), k):
                grp = s[idx:idx+k]
                curr += str(sum(int(num) for num in grp))
            s = curr

        return s
