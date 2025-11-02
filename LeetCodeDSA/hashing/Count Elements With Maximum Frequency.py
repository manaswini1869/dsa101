class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        mapper = defaultdict(int)
        max_freq = 0
        count = 0

        for num in nums:
            mapper[num] += 1
            freq = mapper[num]

            if freq > max_freq:
                max_freq = freq
                count = freq
            elif freq == max_freq:
                count += freq

        # for v in mapper.values():
        #     if v == max_freq:
        #         count += v

        return count

