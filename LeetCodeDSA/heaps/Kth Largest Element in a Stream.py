class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []
        for num in nums:
            heapq.heappush(self.max_heap, num)
            if len(self.max_heap) > k:
                heapq.heappop(self.max_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, val)
        while self.max_heap and len(self.max_heap) > self.k:
            heapq.heappop(self.max_heap)

        return self.max_heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)