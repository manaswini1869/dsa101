class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = []
        tmp = [nums[0]]
        start = nums[0]

        for i in range(1, n):
            if nums[i] - start <= k:
                tmp.append(nums[i])
            else:
                res.append(tmp)
                tmp = [nums[i]]
                start = nums[i]
        res.append(tmp)
        return len(res)


