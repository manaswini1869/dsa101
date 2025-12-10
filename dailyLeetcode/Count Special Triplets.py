class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9+7
        count = 0
        mapper = defaultdict(list)

        for i, v in enumerate(nums):
            mapper[v].append(i)

        for i in range(1, n-1):
            mid = nums[i] * 2
            if mid not in mapper:
                continue

            idx_list = mapper[mid]
            left = bisect_left(idx_list, i)
            right = len(idx_list) - bisect_right(idx_list, i)
            count += (left*right)
        return count % MOD
