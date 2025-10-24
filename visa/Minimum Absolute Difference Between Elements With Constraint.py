class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)

        ans = float("inf")

        # for i in range(n):
        #     for j in range(i+x, n):
        #         ans = min(ans, abs(nums[i] - nums[j]))

        # return ans

        visit = SortedList()

        for j in range(n):
            if j - x >= 0:
                visit.add(nums[j-x])

            if visit:
                idx = visit.bisect_left(nums[j])
                if idx < len(visit):
                    ans = min(ans, abs(nums[j] - visit[idx]))
                if idx > 0:
                    ans = min(ans, abs(nums[j] - visit[idx - 1]))


        return ans



