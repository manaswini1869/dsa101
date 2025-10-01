class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < k:
            return False

        freq_map = {}
        max_freq = float("-inf")
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
            if max_freq < freq_map[num]:
                max_freq = freq_map[num]
            if max_freq * k > n:
                return False

        return max_freq * k <= n
