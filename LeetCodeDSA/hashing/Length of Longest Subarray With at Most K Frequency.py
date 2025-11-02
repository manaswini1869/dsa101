class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        n = len(nums)
        mapper = defaultdict(int)
        count = 0
        left = 0

        for right in range(n):
            mapper[nums[right]] += 1

            if mapper[nums[right]] == k+1:
                count += 1

            if count:
                mapper[nums[left]] -= 1
                if mapper[nums[left]] == k:
                    count -= 1
                left += 1

        return n - left



        # counting + sliding window approach (nested approach)
        # mapper = defaultdict(int)
        # left = 0
        # mapper[nums[left]] += 1

        # n = len(nums)
        # max_len = 1

        # for right in range(1, n):
        #     mapper[nums[right]] += 1

        #     while mapper[nums[right]] > k and left < right:
        #         mapper[nums[left]] -= 1
        #         left += 1
        #     max_len = max(max_len, right - left + 1)

        # return max_len



