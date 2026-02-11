from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        n = len(nums)
        if n < 2:
            return 0
        left = 0
        count = 0
        even, odd = set(), set()
        if nums[left] % 2 == 0:
            even.add(nums[left])
        else:
            odd.add(nums[left])

        for right in range(1, n):
            while even and nums[right] in even:
                even.remove(nums[left])
                left += 1
            while odd and nums[right] in odd:
                odd.remove(nums[left])
                left += 1
            count = max(count, right - left + 1)
            if nums[right] % 2 == 0:
                even.add(nums[right])
            else:
                odd.add(nums[right])
        return count
            

        

        # count = 0
        # n = len(nums)

        # for i in range(n):
        #     odd, even = set(), set()
        #     for j in range(i, n):
        #         if nums[j] % 2 == 0:
        #             even.add(nums[j])
        #         else:
        #             odd.add(nums[j])
        #         if len(even) == len(odd):
        #             count = max(count, j - i + 1)

        # return count

        # # time complexity = O(n**2)
        # # space complexit = O(n)




        