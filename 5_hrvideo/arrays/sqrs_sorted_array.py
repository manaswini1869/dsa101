class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # return sorted([num*num for num in nums])

        if not nums:
            return nums

        if nums[0] >= 0:
            return [num**2 for num in nums]

        idx = -1
        for i, v in enumerate(nums):
            if v >= 0:
                idx = i
                break
        A = nums[idx:]
        B = [-1*num for num in nums[:idx][::-1]]
        res = []
        left, right = 0, 0

        while left < len(A) and right < len(B):
            if A[left] < B[right]:
                res.append(A[left]**2)
                left += 1
            else:
                res.append(B[right]**2)
                right += 1

        while left < len(A):
            res.append(A[left]**2)
            left += 1
        while right < len(B):
            res.append(B[right]**2)
            right += 1

        return res


