class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bitwise = 0
        no_subset = 0
        n = len(nums)
        for num in nums:
            max_bitwise |= num

        def dfs(index, curr_or):
            nonlocal no_subset
            if index == n:
                if curr_or == max_bitwise:
                    no_subset += 1
                return
            dfs(index + 1, curr_or | nums[index])
            dfs(index + 1, curr_or)
        dfs(0, 0)

        return no_subset