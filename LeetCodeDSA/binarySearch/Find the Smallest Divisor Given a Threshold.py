class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        left = 1
        right = 10**6

        while left < right:
            mid = (left+right) // 2
            curr = 0
            for num in nums:
                curr += ceil(num / mid)
            if curr <= threshold:
                right = mid
            else:
                left = mid + 1
        return left







