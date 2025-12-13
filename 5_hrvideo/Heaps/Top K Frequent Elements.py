class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        for num in nums:
            mapper[num] = mapper.get(num, 0) + 1

        stack = []
        for i, v in mapper.items():
            heapq.heappush(stack, (v, i))
            if len(stack) > k:
                heapq.heappop(stack)

        return [i for _, i in stack]











