class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        n = len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            curr = set()
            for j in range(i+1, n):
                if target-nums[j] in curr:
                    res.add((nums[i], target-nums[j], nums[j]))
                curr.add(nums[j])
        print(res)
        return [list(r) for r in res]


