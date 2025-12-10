class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        n = len(nums)
        nums = sorted(nums)
        for i in range(n-2):
            target = -1*nums[i]
            left, right = i+1, n-1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1


        return list(res)


