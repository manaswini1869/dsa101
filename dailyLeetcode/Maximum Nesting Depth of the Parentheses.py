from queue import Queue

class Solution:
    def maxDepth(self, s: str) -> int:

        res = 0
        q = []

        for ch in s:
            if ch == '(':
                q.append(ch)
            res = max(res, len(q))

            if ch == ')':
                q.pop()
        return res


        