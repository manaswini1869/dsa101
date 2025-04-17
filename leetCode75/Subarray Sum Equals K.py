class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # count_sub = 0
        # for i in range(n):
        #     curr_sum = 0
        #     for j in range(i, n):
        #         curr_sum += nums[j]
        #         if curr_sum == k:
        #             count_sub += 1
        # return count_sub
        count = 0
        curr_sum = 0
        sum_hash = {}
        sum_hash[0] = 1
        n = len(nums)
        for i in range(n):
            curr_sum += nums[i]
            if curr_sum-k in sum_hash:
                count += sum_hash[curr_sum-k]
            sum_hash[curr_sum] = sum_hash.get(curr_sum, 0) + 1
        return count

