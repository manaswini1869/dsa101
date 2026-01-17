class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        n = len(nums)

        curr_sum = 0
        tracker = defaultdict(int)
        tracker[0] = 1

        for num in nums:
            curr_sum += num
            if curr_sum - k in tracker:
                count += tracker[curr_sum - k]
            tracker[curr_sum] += 1
        return count



