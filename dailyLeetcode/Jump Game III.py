from collections import deque
from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        q = deque([start])
        visit = set([start])
        n = len(arr)

        while q:
            curr = q.popleft()
            if arr[curr] == 0:
                return True
            
            for nidx in (curr + arr[curr], curr-arr[curr]):
                if 0 <= nidx < n and nidx not in visit:
                    q.append(nidx)
                    visit.add(nidx)
        
        return False


        