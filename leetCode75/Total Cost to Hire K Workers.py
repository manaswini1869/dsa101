import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = 0, len(costs) - 1
        left_heap, right_heap = [], []
        total = 0

        # Preload initial candidates into heaps
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, (costs[left], left))
                left += 1
            if left <= right:
                heapq.heappush(right_heap, (costs[right], right))
                right -= 1

        for _ in range(k):
            # Decide which heap to pull from
            if not right_heap or (left_heap and left_heap[0][0] <= right_heap[0][0]):
                cost, _ = heapq.heappop(left_heap)
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1
            else:
                cost, _ = heapq.heappop(right_heap)
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1
            total += cost

        return total
