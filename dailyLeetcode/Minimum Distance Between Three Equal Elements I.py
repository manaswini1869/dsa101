class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        g = defaultdict(list)

        for i, x in enumerate(nums):
            g[x].append(i)
        
        ans = float("inf")

        for ls in g.values():
            for h in range(len(ls)-2):
                i, k = ls[h], ls[h+2]
                ans = min(ans, (k-i)*2)

        # n = len(nums)

        # ans = float("inf")

        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] == nums[j] == nums[k]:
        #                 ans = min(ans, (
        #                     abs(i-j) + abs(j-k) + abs(i-k)
        #                 ))


        return -1 if ans == float("inf") else ans
        