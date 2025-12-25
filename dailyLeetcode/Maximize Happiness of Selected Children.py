class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:


        n = len(happiness)
        happy = 0
        rounds = 0
        max_heap = []
        for h in happiness:
            heapq.heappush(max_heap, -h)

        while k>0:
            curr = heapq.heappop(max_heap)
            curr *= -1
            curr -= rounds
            if curr > 0:
                happy += curr
            k -= 1
            rounds += 1
        return happy









