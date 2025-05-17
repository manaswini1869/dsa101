class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # color_map = {0: 0, 1:0, 2:0}
        # n = len(nums)
        # for i in nums:
        #     color_map[i] += 1
        # i = 0
        # for k, v in color_map.items():
        #     j = 0
        #     while j < v and i < n:
        #         nums[i] = k
        #         j += 1
        #         i += 1

        n = len(nums)
        p0 = 0
        p2 = n - 1
        curr = 0
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

