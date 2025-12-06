class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)
        if n < 3:
            return 'Radiant' if senate[0]=='R' else 'Dire'

        rq = deque()
        dq = deque()

        for i in range(n):
            if senate[i] == 'R':
                rq.append(i)
            else:
                dq.append(i)

        i, j = 0, 0
        nr, nd = len(rq), len(dq)
        while rq and dq:
            r, d = rq.popleft(), dq.popleft()
            if r < d:
                rq.append(r+n)
            else:
                dq.append(d+n)
        return "Radiant" if rq else "Dire"


