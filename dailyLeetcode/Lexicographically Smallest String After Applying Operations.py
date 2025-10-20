class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = deque()
        q.append(s)
        vis = set(s)
        ans = s

        while q:
            temp = q.popleft()
            if ans > temp:
                ans = temp
            t1 = ''.join([str((int(c) + a) % 10) if i & 1 else c for i, c in enumerate(temp)])
            t2 = temp[-b:] + temp[:-b]

            for t in (t1, t2):
                if t not in vis:
                    q.append(t)
                    vis.add(t)

        return ans
