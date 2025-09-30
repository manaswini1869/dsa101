class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]

        if len(nums) == 2 or len(nums) == 3:
            return max(nums)

        def prob(arr):
            prev1 = arr[0]
            prev2 = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                curr = max(prev2, prev1 + arr[i])
                prev1, prev2 = prev2, curr

            return prev2


        return max(prob(nums[1:]), prob(nums[:-1]))