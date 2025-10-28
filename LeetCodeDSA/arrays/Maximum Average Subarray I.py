class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        curr_max = res_max = sum(nums[:k])
        print(nums[:k])
        left = 0

        for i in range(k, n):
            curr_max = curr_max - nums[left] + nums[i]
            res_max = max(res_max, curr_max)
            left += 1
        return res_max / k

