from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        current_pairs = 0
        left = 0
        counter_map = defaultdict(int)
        for right in range(n):
            num_right = nums[right]
            current_pairs +=  counter_map[num_right]
            counter_map[num_right] += 1
            while current_pairs >= k:
                nums_left = nums[left]
                counter_map[nums_left] -= 1
                current_pairs -= counter_map[nums_left]
                left += 1
            count += left
        return count