class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if i < j and j-i != nums[j] - nums[i]:
        #             res += 1
        # return res
        n = len(nums)
        total_pairs = n * (n-1) // 2

        count_map = defaultdict(int)
        good_pair = 0

        for i, num in enumerate(nums):
            diff = num - i
            good_pair += count_map[diff]
            count_map[diff] += 1
        return total_pairs - good_pair