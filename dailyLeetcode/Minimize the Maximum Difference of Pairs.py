class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        def can_form(max_mid):
            count = 0
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= max_mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if can_form(mid):
                right = mid
            else:
                left = mid + 1
        return left
