class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_map = {}
        max_freq = float("-inf")
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
            max_freq = max(hash_map[num], max_freq)
        print(max_freq)
        res = 0
        for val in hash_map.values():
            if val == max_freq:
                res += val

        return res
