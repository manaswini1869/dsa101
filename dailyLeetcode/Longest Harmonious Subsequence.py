class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # left = 0
        # res = float('-inf')
        # nums = sorted(nums)
        # for right in range(n):
        #     while nums[right] - nums[left] > 1:
        #         left += 1
        #     if nums[right] - nums[left] == 1:
        #         res = max(res, right - left + 1)

        # return res if res != float('-inf') else 0
        res_map = defaultdict(int)
        for i in nums:
            res_map[i] += 1

        res = 0
        for key, val in res_map.items():
            if key+1 in res_map:
                res = max(res, val + res_map[key+1])
        return res


