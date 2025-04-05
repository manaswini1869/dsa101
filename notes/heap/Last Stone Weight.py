class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones = sorted(stones)
        # while len(stones) > 1:
        #     larg, lar = stones.pop(), stones.pop()
        #     print(larg, lar, stones)
        #     if larg == lar:
        #         continue
        #     else:
        #         dif = abs(larg-lar)
        #         stones.append(dif)
        #         stones.sort()
        # return stones[0] if stones else 0
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -1*stone)
        while len(maxHeap) > 1:
            larg, lar = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, larg + (-1*lar))
        return -1*maxHeap[0] if maxHeap else 0

