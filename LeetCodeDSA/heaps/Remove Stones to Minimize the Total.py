class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        max_heap = []

        for pile in piles:
            heapq.heappush(max_heap, -pile)

        while k:
            k -= 1
            rem = heapq.heappop(max_heap)
            heapq.heappush(max_heap, rem // 2)

        return -sum(max_heap)






