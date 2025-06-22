class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq_map = defaultdict(int)
        for i in word:
            freq_map[i] += 1

        res = float('inf')
        freq = sorted(list(freq_map.values()))
        n = len(freq)
        for i in range(n):
            deletions = 0
            base = freq[i]
            for j in freq:
                if j < base:
                    deletions += j
                elif j > base + k:
                    deletions += j - (base+k)
            res = min(res, deletions)
        return res