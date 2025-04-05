class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        minHeap = []
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        print(freq_map)
        for key, val in freq_map.items():
            heapq.heappush(minHeap, (val, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [ele for fre, ele in minHeap]