class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        odd_freq = float('-inf')
        even_freq = float('inf')
        for fre in freq.values():
            if fre % 2 != 0 and fre > odd_freq:
                odd_freq = fre
            if fre % 2 == 0 and fre < even_freq:
                even_freq = fre

        return odd_freq - even_freq