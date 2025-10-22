class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()

        # n = len(nums)
        # res = []
        # freq = Counter(nums)
        # j = 0
        # for i in range(3):
        #     while freq[i]:
        #         nums[j] = i
        #         freq[i] -= 1
        #         j += 1

        n = len(nums)
        l, r = 0, 1
        while r < n:
            if nums[r] < nums[l]:
                nums[l], nums[r] = nums[r], nums[l]
                if l > 0:
                    l -= 1
                    r -= 1
            else:
                l += 1
                r += 1
