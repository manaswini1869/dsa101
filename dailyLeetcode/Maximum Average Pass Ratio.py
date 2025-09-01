import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return (p+1)/(t+1) - p/t

        max_heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(max_heap)

        while extraStudents > 0:
            g, p, t = heapq.heappop(max_heap)
            p, t = p+1, t+1
            heapq.heappush(max_heap, (-gain(p, t), p, t))
            extraStudents -= 1

        total_ratios = sum(p /t for _,p, t in max_heap)
        return total_ratios / len(classes)
