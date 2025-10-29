

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        avgs = [-1] * n

        if n < k:
            return avgs

        p = [nums[0]]

        for i in range(1, n):
            p.append(p[-1] + nums[i])

        left = -1
        for i in range(k, n):
            j = i + k
            m = abs(i - k) - 1

            if 0 <= j < n:
                if m < 0:
                    avgs[i] = (p[j]) // (2*k + 1)
                else:
                    avgs[i] = (p[j] - p[m]) // (2*k + 1)





        return avgs

