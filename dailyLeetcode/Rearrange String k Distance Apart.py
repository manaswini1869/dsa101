from collections import Counter, deque
import heapq
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        
        counter = Counter(s)

        max_heap = []
        for ch, freq in counter.items():
            heapq.heappush(max_heap, (-freq ,ch))

        q = deque()
        ans = []
        while max_heap:
            freq, ch = heapq.heappop(max_heap)
            freq *= -1
            ans.append(ch)
            q.append((freq-1, ch))

            if len(q) >= k:
                freq, ch = q.popleft()
                if freq > 0:
                    heapq.heappush(max_heap, (-freq, ch))

        return "" if len(ans) != len(s) else "".join(ans)  



        