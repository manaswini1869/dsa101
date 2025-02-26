from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count_odd = 0
        count_even = 1
        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2:
                result += count_even
                count_odd += 1
            else:
                result += count_odd
                count_even += 1

            result %= MOD

        return result