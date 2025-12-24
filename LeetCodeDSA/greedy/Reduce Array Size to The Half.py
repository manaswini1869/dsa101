class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        n = len(arr)
        freq_mapper = {}

        for num in arr:
            freq_mapper[num] = freq_mapper.get(num, 0) + 1

        heap = []
        for key, val in freq_mapper.items():
            heapq.heappush(heap, (-val, key))
        ans = 0
        curr_size = n
        target = n // 2
        while curr_size > target:
            freq, val = heapq.heappop(heap)
            ans += 1
            curr_size += freq

        return ans











