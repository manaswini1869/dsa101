class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        for i in range(1, n):
            if (i%2 == 1 and nums[i] < nums[i-1]) or (i%2==0 and nums[i] > nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]



        # O(logn)
        # n = len(nums)
        # sorted_nums = sorted(nums)
        # i, j = 0, n-1
        # k = 0
        # while k < n:
        #     if k % 2 == 0:
        #         nums[k] = sorted_nums[i]
        #         i += 1
        #     else:
        #         nums[k] = sorted_nums[j]
        #         j -= 1
        #     k += 1








