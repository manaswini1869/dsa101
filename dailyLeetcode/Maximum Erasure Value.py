from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        current_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                # Remove nums[left] to shrink window until duplicate removed
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            # Add the new element
            seen.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)

        return max_sum
