from collections import Counter
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        freq = Counter(nums)
        for num in list(freq.keys()):
            complement = k - num
            if complement in freq:
                if complement == num:
                    pairs = freq[num] // 2
                else:
                    pairs = min(freq[num], freq[complement])
                count += pairs
                freq[num] -= pairs
                freq[complement] -= pairs
        return count
