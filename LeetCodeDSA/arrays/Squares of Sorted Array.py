class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [0]*n

        left, right = 0, n-1

        pos = n-1

        while left <= right:
            if abs(nums[right]) < abs(nums[left]):
                res[pos] = nums[left]*nums[left]
                left += 1
            else:
                res[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1

        return res








#         res = []

#         left = 0

#         for num in nums:
#             res.append(num*num)
#         res.sort()
#         return res



