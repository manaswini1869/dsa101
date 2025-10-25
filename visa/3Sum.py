class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        n = len(nums)
        nums.sort()

        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add(tuple(sorted((nums[i], nums[j], nums[k]))))

        for i in range(n):
            target = -nums[i]
            curr = set()
            for j in range(i+1, n):
                v = nums[j]
                if target - v in curr:
                    res.add(((nums[i], v, target-v)))
                curr.add(nums[j])
        return list(res)

