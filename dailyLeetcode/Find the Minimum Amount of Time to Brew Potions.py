class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        times = [0]*n

        for j in range(m):
            curr = 0
            for i in range(n):
                curr = max(times[i], curr) + skill[i] * mana[j]
            times[n-1] = curr
            for i in range(n-2, -1, -1):
                times[i] = times[i+1] - skill[i+1] * mana[j]
        return times[n-1]



