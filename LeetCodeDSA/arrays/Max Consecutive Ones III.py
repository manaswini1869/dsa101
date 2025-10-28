class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_ones = 0
        n = len(nums)

        curr_zeroes = 0

        for right in range(n):
            if nums[right] == 0:
                curr_zeroes += 1

            while curr_zeroes > k:
                if nums[left] == 0:
                    curr_zeroes -= 1
                left += 1

            max_ones = max(max_ones, right - left + 1)



        return max_ones