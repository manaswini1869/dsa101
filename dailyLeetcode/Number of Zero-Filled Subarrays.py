class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        current = 0
        count = 0

        for num in nums:
            if num == 0:
                current += 1
                count += current
            else:
                current = 0

        return count