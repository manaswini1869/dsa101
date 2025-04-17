class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # max_len = 0
        # for i in range(n):
        #     curr_sum = 0
        #     for j in range(i, n):
        #         curr_sum += nums[j]
        #         if curr_sum == k:
        #             max_len = max(max_len, j - i + 1)
        # return max_len
        prefix_sum = 0
        max_len = 0
        hash_map = {}
        for i, num in enumerate(nums):
            prefix_sum += num
            req = prefix_sum - k
            if prefix_sum == k:
                max_len = i + 1
            if req in hash_map:
                max_len = max(max_len, i - hash_map[req])
            if prefix_sum not in hash_map:
                hash_map[prefix_sum] = i
        return max_len
