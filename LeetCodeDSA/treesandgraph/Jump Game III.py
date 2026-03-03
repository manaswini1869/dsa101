class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        seen = set([start])
        q = deque([start])
        n = len(arr)

        while q:
            curr = q.popleft()
            if arr[curr] == 0:
                return True
            for nxt in (curr+arr[curr], curr-arr[curr]):
                if 0 <= nxt < n and nxt not in seen:
                    q.append(nxt)
                    seen.add(nxt)

        return False







