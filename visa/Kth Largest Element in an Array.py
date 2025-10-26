class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        stack = []
        for num in nums:
            heapq.heappush(stack, -num)
        res = 0
        while k > 0:
            res = heapq.heappop(stack)
            k -= 1

        return -1 * res


