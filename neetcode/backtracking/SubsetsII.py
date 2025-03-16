class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def subset(i, cur):
            if i == len(nums):
                res.append(cur[::])
                return
            cur.append(nums[i])
            subset(i+1, cur)
            cur.pop()

            while (i+1 < len(nums)) and (nums[i] == nums[i+1]):
                i += 1 #skipping the duplicates
            subset(i+1, cur)
        subset(0, [])
        return res
