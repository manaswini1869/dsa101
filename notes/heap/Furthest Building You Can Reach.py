class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        for i in range(len(heights)-1):
            current_height = heights[i]
            next_height = heights[i+1]
            diff = next_height - current_height
            if diff <= 0:
                continue
            heapq.heappush(min_heap, diff)
            if len(min_heap) <= ladders:
                continue
            bricks -= heapq.heappop(min_heap)
            if bricks < 0:
                return i
        return len(heights) - 1