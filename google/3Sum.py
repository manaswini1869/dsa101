class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        res, temp = [], []

        def ksum(start, k, target):
            if k != 2:
                for i in range(start, n):
                    if i > start and nums[i-1] == nums[i]:
                        continue
                    temp.append(nums[i])
                    ksum(i+1, k-1, target-nums[i])
                    temp.pop()
                return

            left, right = start, n-1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append((temp + [nums[left], nums[right]]))
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1


        ksum(0, 3, 0)
        return res


        # nums.sort()
        # n = len(nums)
        # res = set()

        # hash_map = {}
        # for i in range(n):
        #     seen = set()
        #     for j in range(i+1, n):
        #         target = -nums[i]-nums[j]
        #         if target in seen:
        #             res.add((target, nums[i], nums[j]))
        #         seen.add(nums[j])
        # return [list(x) for x in res]







