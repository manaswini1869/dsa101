class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        max_heap = [(-cnt, word) for word, cnt in count.items()]
        heapify(max_heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])

        return res