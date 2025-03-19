class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # n = len(stones)
        # while n > 1:
        #     stones.sort()
        #     cur = stones.pop() - stones.pop()
        #     if cur > 0:
        #         stones.append(cur)
        #         n -= 1
        #     else:
        #         n -= 2
        # return stones[0] if stones else 0
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        return abs(stones[0]) if stones else 0
