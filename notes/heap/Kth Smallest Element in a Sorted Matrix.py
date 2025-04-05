class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(minHeap, -1*matrix[i][j])
                if len(minHeap) > k:
                    heapq.heappop(minHeap)
        print(minHeap)
        return -1*minHeap[0]