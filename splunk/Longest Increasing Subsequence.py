class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        sub = [nums[0]]
        for i in range(1, n):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                j = 0
                while nums[i] > sub[j]:
                    j += 1
                sub[j] = nums[i]
        return len(sub)






