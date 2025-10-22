class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq = defaultdict(int)

        range_contri = defaultdict(int)

        for num in nums:
            freq[num] += 1

            range_contri[num] += 0

            range_contri[num-k] += 1
            range_contri[num+k+1] -= 1

        max_freq = 0
        curr_sum = 0

        for pos, contri in sorted(range_contri.items()):
            curr_sum += contri

            max_freq = max(max_freq, min(curr_sum, freq[pos] + numOperations))

        return max_freq




