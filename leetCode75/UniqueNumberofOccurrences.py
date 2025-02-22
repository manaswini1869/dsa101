class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            freq[i] = 1 + freq.get(i, 0)
        return len(set(freq.values())) == len(freq.values())
